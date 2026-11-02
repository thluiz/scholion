#Requires -Version 7
# Rotina diária (task \Claude\KindleImport, 04:00): lê library/ (o sync das 01:00 já rodou) e, para cada livro de
# books.json, importa os destaques novos como notas quote (mode=auto) ou só avisa (mode=notify).
# Sem LLM: gerar -> conferir (verify.py) -> gravar (save.ps1, um commit por nota) -> push -> aviso no GossipGate.
param(
  [string] $Registry = (Join-Path (Split-Path -Parent $PSScriptRoot) 'books.json'),
  [switch] $DryRun,            # gera e confere em pasta temporária; não grava, não commita, não dá push
  [int] $MaxPerBook = 40       # acima disso não importa sozinha: avisa para rodar a skill (evita despejo em massa)
)
$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [Text.Encoding]::UTF8
$OutputEncoding = [Text.Encoding]::UTF8
$env:PYTHONIOENCODING = 'utf-8'
$repo = 'E:\scholion'
$skill = Split-Path -Parent $PSScriptRoot
$scripts = $PSScriptRoot
$lib = 'E:\kindle-scrapper\library'
$work = Join-Path $env:TEMP 'kindle-import'
$logDir = Join-Path $env:LOCALAPPDATA 'scholion-kindle-import'
New-Item -ItemType Directory -Force $work, $logDir | Out-Null
$logFile = Join-Path $logDir 'auto-import.log'
$py = (Get-Command python -ErrorAction SilentlyContinue)?.Source
if (-not $py) { $py = 'C:\Users\conta\AppData\Local\Programs\Python\Python312\python.exe' }

function Log($m) { "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')  $m" | Tee-Object -FilePath $logFile -Append }
function Notify($msg) {
  if ($DryRun) { Log "[dry-run] aviso: $msg"; return }
  try {
    $key = (Get-Content 'C:\Users\conta\.gossipgate\api-key' -Raw).Trim()
    $body = @{ message = $msg } | ConvertTo-Json -Compress
    Invoke-RestMethod -Uri 'http://localhost:8080/api/gossip-gate/send' -Method Post `
      -Headers @{ 'X-Api-Key' = $key } -ContentType 'application/json' -Body $body | Out-Null
  } catch { Log "Falha ao notificar: $($_.Exception.Message)" }
}

$avisos = @(); $gravadas = 0
try {
  Log "=== auto-import $(if ($DryRun) { '(dry-run)' }) ==="
  if (-not $DryRun) { git -C $repo pull --ff-only 2>&1 | Out-Null }   # melhor esforço; falha não aborta
  $reg = Get-Content -Raw -Encoding UTF8 $Registry | ConvertFrom-Json
  foreach ($b in $reg.books) {
    $slug = $b.library
    $libFile = Join-Path $lib "$slug.md"
    if (-not (Test-Path $libFile)) { $avisos += "⚠️ ${slug}: arquivo não está em library/"; continue }
    $anthology = [bool]$b.anthology
    $plain = if ($anthology) { @() } else { @('--plain') }
    $wd = Join-Path $work $slug
    Remove-Item -Recurse -Force $wd -ErrorAction SilentlyContinue
    New-Item -ItemType Directory -Force "$wd\drafts" | Out-Null

    # 1) pendentes (cruza com TODAS as notas do vault)
    & $py -I "$scripts\crossmatch.py" $libFile --json "$wd\hl.json" @plain | Out-Null
    if ($LASTEXITCODE -ne 0) { $avisos += "❌ ${slug}: crossmatch falhou"; continue }
    $bookJson = $b | Select-Object title, short_title, author, publisher, year, tag, anthology
    ($bookJson | ConvertTo-Json -Compress) | Set-Content -Encoding UTF8 "$wd\book.json"

    # 2) gerar (sem --confirm: autoria nunca é inventada)
    $skip = ($b.ignore_locs -join ',')
    $gargs = @('--lib', $libFile, '--hl', "$wd\hl.json", '--out', "$wd\drafts", '--book', "$wd\book.json")
    if ($skip) { $gargs += @('--skip', $skip) }
    if ($b.since) { $gargs += @('--since', $b.since) }
    $gout = (& $py -I "$scripts\generate.py" @gargs 2>&1 | Out-String)
    $gexit = $LASTEXITCODE
    if ($gexit -notin 0, 2) { $avisos += "❌ ${slug}: generate.py falhou"; Log $gout; continue }
    $m = [regex]::Match($gout, 'gerados=(\d+) pendencias=(\d+)')
    $n = [int]$m.Groups[1].Value; $pend = [int]$m.Groups[2].Value
    Log "${slug}: gerados=$n pendencias=$pend modo=$($b.mode)"
    $pendTxt = ($gout -split "`n" | Where-Object { $_ -like 'PENDENTE*' } | Select-Object -First 3) -join ' | '

    if ($b.mode -ne 'auto') {
      if ($n + $pend -gt 0) { $avisos += "📚 $($b.short_title): $($n + $pend) destaque(s) novo(s) aguardando você (rode a skill import-kindle-highlights)." }
      continue
    }
    if ($n -eq 0) {
      if ($pend -gt 0) { $avisos += "⚠️ $($b.short_title): $pend destaque(s) não importado(s): $pendTxt" }
      continue
    }
    if ($n -gt $MaxPerBook) {
      $avisos += "📚 $($b.short_title): $n destaques novos (> $MaxPerBook); importe pela skill import-kindle-highlights."
      continue
    }
    if ($DryRun) { $avisos += "[dry-run] $($b.short_title): importaria $n nota(s), $pend pendência(s)";
      & $py -I "$scripts\verify.py" $libFile $b.tag --drafts "$wd\drafts" @plain | Select-Object -First 3 | ForEach-Object { Log $_ }
      continue }

    # 3) página do livro (uma vez)
    $tagIdx = "$repo\content\tags\$($b.tag)\_index.md"
    if (-not (Test-Path $tagIdx)) {
      New-Item -ItemType Directory -Force (Split-Path $tagIdx) | Out-Null
      $meta = "  author: `"$($b.author)`""
      if ($b.publisher) { $meta += "`n  publisher: `"$($b.publisher)`"" }
      if ($b.year) { $meta += "`n  year: $($b.year)" }
      $idx = "---`ntitle: `"$($b.title -replace '"','\"')`"`ndescription: `"Citações guardadas de $($b.author).`"`nbook:`n$meta`n---`n"
      [IO.File]::WriteAllText($tagIdx, $idx, (New-Object Text.UTF8Encoding($false)))
      git -C $repo add "content/tags/$($b.tag)/_index.md" 2>&1 | Out-Null
      git -C $repo commit -q --only -m "site: página do livro $($b.short_title)" -- "content/tags/$($b.tag)/_index.md" 2>&1 | Out-Null
    }

    # 4) gravar (save.ps1 roda verify.py antes e aborta em ERRO)
    $sargs = @{ Drafts = "$wd\drafts"; Lib = $libFile; Tag = $b.tag; Scratch = $wd }
    if (-not $anthology) { $sargs.Plain = $true }
    $res = & "$scripts\save.ps1" @sargs
    $gravadas += $n
    $msg = "📖 $($b.short_title): $n nota(s) nova(s) importada(s)."
    if ($pend -gt 0) { $msg += " $pend não importada(s): $pendTxt" }
    $avisos += $msg
  }

  if ($gravadas -gt 0 -and -not $DryRun) {
    $push = (git -C $repo push 2>&1 | Out-String)
    if ($LASTEXITCODE -ne 0) { $avisos += "❌ push falhou: $($push.Trim().Split("`n")[-1])" }
    else { Log "push ok ($gravadas notas)" }
  }
  if ($avisos.Count -gt 0) { Notify (($avisos) -join "`n") }
  Log "fim: gravadas=$gravadas avisos=$($avisos.Count)"
} catch {
  Log "ERRO: $($_.Exception.Message)"
  Notify "❌ Kindle import falhou: $($_.Exception.Message)"
  exit 1
}
