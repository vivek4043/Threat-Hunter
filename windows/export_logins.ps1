Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4624} |
Select-Object TimeCreated, @{Name="User";Expression={$_.Properties[5].Value}} |
Export-Csv -Path "logins.csv" -NoTypeInformation
