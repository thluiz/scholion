#Requires -Version 7
param(
    [switch]$SkipBuild,
    [switch]$ForceFullSync
)

$ErrorActionPreference = "Stop"

$REPO_DIR    = "E:\scholion"
$PUBLIC_DIR  = "$REPO_DIR\public"
$MANIFEST    = "$REPO_DIR\public-manifest.json"
$LAST_COMMIT = "$REPO_DIR\last-published-commit.txt"

$AWS_PROFILE = "scholion-admin"
$BUCKET      = "s3://scholion-thluiz-com"
$CF_ID       = "E3LDBL5EPS3GA2"
$REGION      = "us-east-1"
$AWS_EXE     = (Get-Command aws -ErrorAction Stop).Source

function aws { & $AWS_EXE --profile $AWS_PROFILE --region $REGION @args }

# Build
if (-not $SkipBuild) {
    Write-Host "==> hugo build" -ForegroundColor Cyan
    Set-Location $REPO_DIR
    hugo --minify --gc
    if ($LASTEXITCODE -ne 0) { throw "Hugo build failed" }
}

# Estado anterior
$prevManifest = @{}
if (Test-Path $MANIFEST) {
    $prevManifest = Get-Content $MANIFEST -Raw | ConvertFrom-Json -AsHashtable
}

$currentCommit = (git rev-parse HEAD).Trim()
$lastCommit    = if (Test-Path $LAST_COMMIT) { (Get-Content $LAST_COMMIT -Raw).Trim() } else { $null }

# Verificar se o commit anterior ainda existe (ex: após rebase)
if ($lastCommit) {
    git cat-file -e "$lastCommit^{commit}" 2>$null
    if ($LASTEXITCODE -ne 0) { $lastCommit = $null }
}

# Derivar caminhos a verificar a partir do git diff
function Get-PathsToCheck {
    param($repoDir, $publicDir, $lastCommit, $currentCommit)

    $paths = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)

    # Raízes globais: sempre verificar
    @('index.html', 'index.json', 'index.xml', '404.html', 'sitemap.xml', 'robots.txt') | ForEach-Object {
        if (Test-Path (Join-Path $publicDir $_)) { $paths.Add($_) | Out-Null }
    }

    if (-not $lastCommit -or $lastCommit -eq $currentCommit) { return $paths }

    $changed = git -C $repoDir diff --name-only $lastCommit $currentCommit 2>$null |
               Where-Object { $_ -match '^(content/.*\.md|data/git_history/.*\.json)$' }

    foreach ($f in $changed) {
        # Histórico: data/git_history/slug_com_underscores.json → nota correspondente
        if ($f -match '^data/git_history/(.+)\.json$') {
            $slug = $Matches[1] -replace '_', '-'
            foreach ($section in @('notes', 'research')) {
                $htmlRel = "$section\$slug\index.html"
                if (Test-Path (Join-Path $publicDir $htmlRel)) { $paths.Add($htmlRel) | Out-Null }
            }
            continue
        }
        $name = [System.IO.Path]::GetFileNameWithoutExtension($f)
        $dir  = [System.IO.Path]::GetDirectoryName($f) -replace '/', '\'

        # Leaf:   content\notes\slug.md       → section='notes',  slug='slug'
        # Bundle: content\notes\slug\index.md → section='notes',  slug='slug'
        if ($name -eq 'index') {
            $slug    = Split-Path $dir -Leaf
            $section = ($dir -replace '^content\\', '') -replace '\\[^\\]+$', ''
        } else {
            $slug    = $name
            $section = ($dir -replace '^content\\', '')
        }

        # Todos os arquivos do diretório de saída da nota (index.html, og.webp, imagens, etc.)
        $noteOutDir = Join-Path $publicDir "$section\$slug"
        if (Test-Path $noteOutDir) {
            Get-ChildItem $noteOutDir -File | ForEach-Object {
                $paths.Add($_.FullName.Substring($publicDir.Length + 1)) | Out-Null
            }
        }

        # Lista da seção + paginadores
        $sectionIdx = "$section\index.html"
        if (Test-Path (Join-Path $publicDir $sectionIdx)) { $paths.Add($sectionIdx) | Out-Null }
        $pageDir = Join-Path $publicDir "$section\page"
        if (Test-Path $pageDir) {
            Get-ChildItem $pageDir -Directory | ForEach-Object {
                $p = "$section\page\$($_.Name)\index.html"
                if (Test-Path (Join-Path $publicDir $p)) { $paths.Add($p) | Out-Null }
            }
        }

        # Tags do frontmatter
        $mdFile = Join-Path $repoDir $f
        if (Test-Path $mdFile) {
            $inFront = $false; $inTags = $false; $tags = @()
            foreach ($line in (Get-Content $mdFile)) {
                if ($line -eq '---') {
                    if (-not $inFront) { $inFront = $true } else { break }
                    continue
                }
                if (-not $inFront) { continue }
                if ($line -match '^tags\s*:\s*\[(.+)\]') {
                    $tags = $Matches[1] -split ',' | ForEach-Object { $_.Trim().Trim('"').Trim("'") }; break
                }
                if ($line -match '^tags\s*:')            { $inTags = $true; continue }
                if ($inTags -and $line -match '^\s*-\s*(.+)') { $tags += $Matches[1].Trim() }
                elseif ($inTags) { break }
            }
            foreach ($tag in $tags) {
                $tagSlug = $tag.ToLower() -replace '\s+', '-'
                $tagHtml = "tags\$tagSlug\index.html"
                if (Test-Path (Join-Path $publicDir $tagHtml)) { $paths.Add($tagHtml) | Out-Null }
            }
        }
    }
    return $paths
}

$pathsToCheck = Get-PathsToCheck $REPO_DIR $PUBLIC_DIR $lastCommit $currentCommit
$isFullScan   = $ForceFullSync -or (-not $lastCommit)

if ($isFullScan) {
    Write-Host "==> full scan ($(if ($ForceFullSync) { 'ForceFullSync' } else { 'primeiro deploy' }))" -ForegroundColor Cyan
    $filesToHash = Get-ChildItem $PUBLIC_DIR -Recurse -File | Where-Object { $_.Name -ne '.DS_Store' }
} elseif ($lastCommit -eq $currentCommit) {
    Write-Host "==> sem novos commits — nada a publicar" -ForegroundColor Yellow
    $filesToHash = @()
} else {
    $diffFiles = git diff --name-only $lastCommit $currentCommit
    $nNotes    = ($diffFiles | Where-Object { $_ -match '^content/.*\.md$' } | Measure-Object).Count
    $nHistory  = ($diffFiles | Where-Object { $_ -match '^data/git_history/' } | Measure-Object).Count
    Write-Host "==> incremental — $($pathsToCheck.Count) arquivos ($nNotes notas, $nHistory históricos)" -ForegroundColor Cyan
    $filesToHash = $pathsToCheck | ForEach-Object {
        $full = Join-Path $PUBLIC_DIR $_
        if (Test-Path $full) { Get-Item $full }
    } | Where-Object { $_ }
}

# Hash paralelo das páginas derivadas do diff
$results = $filesToHash | ForEach-Object -Parallel {
    $rel  = $_.FullName.Substring($using:PUBLIC_DIR.Length + 1)
    $hash = (Get-FileHash $_.FullName -Algorithm SHA256).Hash
    [PSCustomObject]@{ Rel = $rel; Hash = $hash }
} -ThrottleLimit 24

$newManifest = $prevManifest.Clone()
$toUpload    = [System.Collections.Generic.List[string]]::new()

foreach ($r in $results) {
    $newManifest[$r.Rel] = $r.Hash
    if ($prevManifest[$r.Rel] -ne $r.Hash) { $toUpload.Add($r.Rel) }
}

# Assets estáticos — sempre re-verificar no modo incremental
if (-not $isFullScan) {
    $assetDirs  = @('css', 'js', 'lib', 'img')
    $assetRoots = @('robots.txt', '404.html', 'index.html', 'sitemap.xml',
                    'favicon.png', 'favicon.ico', 'favicon-16x16.png', 'favicon-32x32.png',
                    'apple-touch-icon.png', 'android-chrome-192x192.png', 'android-chrome-512x512.png')

    $assetFiles = [System.Collections.Generic.List[System.IO.FileInfo]]::new()
    foreach ($d in $assetDirs) {
        $full = Join-Path $PUBLIC_DIR $d
        if (Test-Path $full) { Get-ChildItem $full -Recurse -File | ForEach-Object { $assetFiles.Add($_) } }
    }
    foreach ($f in $assetRoots) {
        $full = Join-Path $PUBLIC_DIR $f
        if (Test-Path $full) { $assetFiles.Add((Get-Item $full)) }
    }

    $assetAdded = 0
    $assetFiles | ForEach-Object -Parallel {
        $rel  = $_.FullName.Substring($using:PUBLIC_DIR.Length + 1)
        $hash = (Get-FileHash $_.FullName -Algorithm SHA256).Hash
        [PSCustomObject]@{ Rel = $rel; Hash = $hash }
    } -ThrottleLimit 16 | ForEach-Object {
        $newManifest[$_.Rel] = $_.Hash
        if ($prevManifest[$_.Rel] -ne $_.Hash -and -not $toUpload.Contains($_.Rel)) {
            $toUpload.Add($_.Rel)
            $script:assetAdded++
        }
    }
    if ($assetAdded -gt 0) { Write-Host "  +$assetAdded asset(s) com hash novo" }
}

# Deleções (só full scan)
$toDelete = [System.Collections.Generic.List[string]]::new()
if ($isFullScan) {
    foreach ($key in $prevManifest.Keys) {
        if (-not (Test-Path (Join-Path $PUBLIC_DIR $key))) {
            $toDelete.Add($key)
            $newManifest.Remove($key) | Out-Null
        }
    }
}

Write-Host "==> upload: $($toUpload.Count) | delete: $($toDelete.Count)" -ForegroundColor Cyan

if ($toUpload.Count -eq 0 -and $toDelete.Count -eq 0) {
    Write-Host "==> sem alterações — skip S3" -ForegroundColor Yellow
} else {
    if ($isFullScan) {
        Write-Host "==> s3 sync HTML (1h cache)..." -ForegroundColor Cyan
        aws s3 sync $PUBLIC_DIR $BUCKET `
            --delete `
            --exclude "*" `
            --include "*.html" --include "*.xml" --include "*.json" --include "*.txt" `
            --cache-control "public, max-age=3600"
        if ($LASTEXITCODE -ne 0) { throw "s3 sync HTML failed" }

        Write-Host "==> s3 sync assets (1y cache)..." -ForegroundColor Cyan
        aws s3 sync $PUBLIC_DIR $BUCKET `
            --exclude "*.html" --exclude "*.xml" --exclude "*.json" --exclude "*.txt" `
            --cache-control "public, max-age=31536000, immutable"
        if ($LASTEXITCODE -ne 0) { throw "s3 sync assets failed" }
    } else {
        $uploadErrors = foreach ($rel in $toUpload) {
            $s3Key = $rel.Replace('\', '/')
            $ct    = if ($rel -match '\.(html|xml|json|txt)$') {
                         "public, max-age=3600"
                     } else {
                         "public, max-age=31536000, immutable"
                     }
            $out = aws s3 cp (Join-Path $PUBLIC_DIR $rel) "$BUCKET/$s3Key" `
                       --cache-control $ct --only-show-errors 2>&1
            if ($LASTEXITCODE -ne 0) { "FAIL: $s3Key — $out" }
        }
        if ($uploadErrors) { throw "Falhas no upload:`n$($uploadErrors -join "`n")" }

        foreach ($rel in $toDelete) {
            aws s3 rm "$BUCKET/$($rel.Replace('\','/'))" | Out-Null
        }
    }

    Write-Host "==> cloudfront invalidation" -ForegroundColor Cyan
    $inv = aws cloudfront create-invalidation `
               --distribution-id $CF_ID `
               --paths "/*" | ConvertFrom-Json
    Write-Host "  $($inv.Invalidation.Id)  $($inv.Invalidation.Status)"
}

# Gravar estado local
$newManifest | ConvertTo-Json -Compress | Set-Content $MANIFEST -Encoding UTF8
$currentCommit | Set-Content $LAST_COMMIT -Encoding UTF8

Write-Host "==> done" -ForegroundColor Green
