Invoke-WebRequest -Uri "https://github.com/arnavryie/d/archive/refs/heads/main.zip" -OutFile "d.zip"
Expand-Archive -Path "d.zip" -DestinationPath "." -Force
Remove-Item "d.zip" -Force
Set-Location "d-main"
Get-ChildItem
Write-Host "All 10 DSL topics imported successfully into d-main!" -ForegroundColor Green
