param(
  [Parameter(Mandatory)] [string] $Drafts,      # pasta com os drafts aprovados
  [Parameter(Mandatory)] [string] $Lib,         # E:\kindle-scrapper\library\<livro>.md
  [Parameter(Mandatory)] [string] $Tag,         # tag do livro
  [Parameter(Mandatory)] [string] $Scratch,     # scratchpad (arquivo de mensagem de commit)
  [string[]] $TagOnly = @(),                    # slugs de notas JÁ existentes que só ganham a tag do livro
  [switch] $Plain                               # livro de autor único (título = destaque inteiro)
)
# Grava as notas aprovadas, uma por commit (--only). NÃO faz push: o push é do passo final da skill.
$ErrorActionPreference = 'Stop'
$repo = 'E:\scholion'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$enc = New-Object Text.UTF8Encoding($false)
$env:PYTHONIOENCODING = 'utf-8'

# 1) Conferência mecânica obrigatória: erro bloqueia tudo (o marcador do gate depende dela).
$plainArg = if ($Plain) { @('--plain') } else { @() }
python -I "$here\verify.py" $Lib $Tag --drafts $Drafts @plainArg
if ($LASTEXITCODE -ne 0) { throw 'verify.py reportou ERRO; nada foi gravado.' }

New-Item -ItemType Directory -Force "$repo\.ghost-audit" | Out-Null

# Outro git no mesmo repo (auto-import, ScholionPublish, outra sessão) deixa .git/index.lock: esperar em vez de
# falhar no meio do lote (2026-11-02: o lote parou na 9ª nota com uma nota só staged).
function Wait-GitLock {
  $lock = "$repo\.git\index.lock"
  for ($i = 0; (Test-Path $lock) -and $i -lt 120; $i++) { Start-Sleep -Seconds 1 }
  if (Test-Path $lock) { throw '.git/index.lock persiste há 2 min; outro git travado? nada mais foi gravado.' }
}

function Git-Retry([string[]] $gitArgs) {
  for ($t = 1; $t -le 5; $t++) {
    Wait-GitLock
    $out = git -C $repo @gitArgs 2>&1 | Where-Object { $_ -notmatch '^warning' }
    if ($LASTEXITCODE -eq 0) { return }
    if (-not ($out -match 'index\.lock')) { $out; throw "git $($gitArgs[0]) falhou" }
    Start-Sleep -Seconds 2
  }
  throw "git $($gitArgs[0]) falhou 5x por lock"
}

function Commit-Note($rel, $msg) {
  $o = git -C $repo rev-parse ":$rel"
  Set-Content -LiteralPath "$repo\.ghost-audit\$o.ok" -Value $o
  $mf = Join-Path $Scratch 'msg.txt'
  [IO.File]::WriteAllText($mf, $msg, $enc)
  Git-Retry @('commit', '-q', '--only', '-F', $mf, '--', $rel)
}

function Strip-Date($s) { [regex]::Replace($s.Replace("`r`n", "`n"), "(?m)^date: '.*'$", "date: ''") }

$log = @()
# 2) Notas novas
foreach ($f in Get-ChildItem "$Drafts\*.md") {
  $slug = $f.BaseName
  $rel = "content/notes/$slug.md"
  $dest = "$repo\content\notes\$slug.md"
  $draft = [IO.File]::ReadAllText($f.FullName, $enc)
  if (Test-Path $dest) {
    # Retomada: nota igual ao draft (fora a data) é deste mesmo lote, gravada antes de uma interrupção.
    $cur = [IO.File]::ReadAllText($dest, $enc)
    if ((Strip-Date $cur) -ne (Strip-Date $draft)) { throw "colisao: $slug (nota existente diferente do draft)" }
    git -C $repo cat-file -e "HEAD:$rel" 2>$null
    if ($LASTEXITCODE -eq 0) { $log += "SKIP $slug (já gravada)"; continue }
    Git-Retry @('add', $rel)
    $title = ([regex]::Match($cur, '(?m)^title: "(.*)"$')).Groups[1].Value.Replace('\"', '"').Replace('\\', '\')
    Commit-Note $rel "note: $title"
    $log += "RESUMED $slug"
    continue
  }
  $date = Get-Date -Format 'yyyy-MM-ddTHH:mm:sszzz'          # hora real, nova a cada nota
  $t = $draft.Replace("date: 'DATE'", "date: '$date'")
  [IO.File]::WriteAllText($dest, $t, $enc)
  Git-Retry @('add', $rel)
  $title = ([regex]::Match($t, '(?m)^title: "(.*)"$')).Groups[1].Value.Replace('\"', '"').Replace('\\', '\')
  Commit-Note $rel "note: $title"
  $log += "NEW $slug"
  Start-Sleep -Seconds 1
}

# 3) Notas já existentes: só a tag do livro
foreach ($slug in $TagOnly) {
  $rel = "content/notes/$slug.md"
  $p = "$repo\content\notes\$slug.md"
  $t = [IO.File]::ReadAllText($p, $enc)
  $m = [regex]::Match($t, '(?m)^tags: \[(.*)\]\s*$')
  if (-not $m.Success) { throw "tags fora do formato [..] em $slug (editar à mão)" }
  if ($m.Value -match [regex]::Escape("`"$Tag`"")) { continue }
  $t = $t.Substring(0, $m.Index) + 'tags: [' + $m.Groups[1].Value + ', "' + $Tag + '"]' + $t.Substring($m.Index + $m.Length)
  [IO.File]::WriteAllText($p, $t, $enc)
  Git-Retry @('add', $rel)
  Commit-Note $rel "note: tag do livro em $slug"
  $log += "TAG $slug"
}
$log
$feitas = @($log | Where-Object { $_ -notlike 'SKIP*' }).Count
Write-Output "Gravadas: $feitas (já gravadas antes: $($log.Count - $feitas)). Falta: git push e conferir contagem com a tag."
