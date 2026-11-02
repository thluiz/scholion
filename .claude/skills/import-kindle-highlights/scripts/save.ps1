param(
  [Parameter(Mandatory)] [string] $Drafts,      # pasta com os drafts aprovados
  [Parameter(Mandatory)] [string] $Lib,         # E:\kindle-scrapper\library\<livro>.md
  [Parameter(Mandatory)] [string] $Tag,         # tag do livro
  [Parameter(Mandatory)] [string] $Scratch,     # scratchpad (arquivo de mensagem de commit)
  [string[]] $TagOnly = @()                     # slugs de notas JÁ existentes que só ganham a tag do livro
)
# Grava as notas aprovadas, uma por commit (--only). NÃO faz push: o push é do passo final da skill.
$ErrorActionPreference = 'Stop'
$repo = 'E:\scholion'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$enc = New-Object Text.UTF8Encoding($false)
$env:PYTHONIOENCODING = 'utf-8'

# 1) Conferência mecânica obrigatória: erro bloqueia tudo (o marcador do gate depende dela).
python -I "$here\verify.py" $Lib $Tag --drafts $Drafts
if ($LASTEXITCODE -ne 0) { throw 'verify.py reportou ERRO; nada foi gravado.' }

New-Item -ItemType Directory -Force "$repo\.ghost-audit" | Out-Null

function Commit-Note($rel, $msg) {
  $o = git -C $repo rev-parse ":$rel"
  Set-Content -LiteralPath "$repo\.ghost-audit\$o.ok" -Value $o
  $mf = Join-Path $Scratch 'msg.txt'
  [IO.File]::WriteAllText($mf, $msg, $enc)
  git -C $repo commit -q --only -F $mf -- $rel 2>&1 | Where-Object { $_ -notmatch '^warning' }
  if ($LASTEXITCODE -ne 0) { throw "commit falhou: $rel" }
}

$log = @()
# 2) Notas novas
foreach ($f in Get-ChildItem "$Drafts\*.md") {
  $slug = $f.BaseName
  $rel = "content/notes/$slug.md"
  $dest = "$repo\content\notes\$slug.md"
  if (Test-Path $dest) { throw "colisao: $slug" }
  $date = Get-Date -Format 'yyyy-MM-ddTHH:mm:sszzz'          # hora real, nova a cada nota
  $t = [IO.File]::ReadAllText($f.FullName, $enc).Replace("date: 'DATE'", "date: '$date'")
  [IO.File]::WriteAllText($dest, $t, $enc)
  git -C $repo add $rel 2>&1 | Where-Object { $_ -notmatch '^warning' }
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
  git -C $repo add $rel 2>&1 | Where-Object { $_ -notmatch '^warning' }
  Commit-Note $rel "note: tag do livro em $slug"
  $log += "TAG $slug"
}
$log
Write-Output "Gravadas: $($log.Count). Falta: git push e conferir contagem com a tag."
