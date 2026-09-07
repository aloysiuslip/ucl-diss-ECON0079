Set-Location "${workspaceFolder}/tex/writing"

$raw = texcount -inc -sum -merge -q -dir=. -template='{sum}' 1_countable.tex 2>$null | Out-String
$num = [regex]::Match($raw, '\d+').Value
$formatted = '{0:N0}' -f [int]$num

Set-Content -Path components/wordcount.tex -Value $formatted -Encoding Ascii

Write-Output $formatted