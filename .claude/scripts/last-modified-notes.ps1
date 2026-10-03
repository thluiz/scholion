<#
.SYNOPSIS
Prints the full paths of the N most recently modified Scholion notes.

.DESCRIPTION
Single source of truth for the "last modified note" default shared by the
style-test, ghost-audit and verify-note skills. Scans E:\scholion\content\notes
recursively for *.md files, skips Hugo section files (_index.md), sorts by
LastWriteTime descending and prints one absolute path per line, newest first.

.PARAMETER Count
How many paths to print. Default: 1.

.EXAMPLE
pwsh -NoProfile -File E:\scholion\.claude\scripts\last-modified-notes.ps1
pwsh -NoProfile -File E:\scholion\.claude\scripts\last-modified-notes.ps1 -Count 3
#>
[CmdletBinding()]
param(
    [ValidateRange(1, 10000)]
    [int]$Count = 1
)

$notesDir = 'E:\scholion\content\notes'

if (-not (Test-Path -LiteralPath $notesDir)) {
    [Console]::Error.WriteLine("notes directory not found: $notesDir")
    exit 1
}

Get-ChildItem -LiteralPath $notesDir -Recurse -File -Filter '*.md' |
    Where-Object { $_.Name -ne '_index.md' } |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First $Count -ExpandProperty FullName
