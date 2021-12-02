function ipss {
	"Ip local: " 
	Get-NetIPAddress -AddressFamily IPv4 -InterfaceAlias Wi-Fi | select -Property IPAddress
	"`nIp publica: " 
	(Invoke-WebRequest -uri "http://ifconfig.me/ip").Content 
}
function encriptar {
	$TEXTO = ipss
	$ENCODED1 = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($TEXTO))
	Write-Output $ENCODED1
}
encriptar | Out-File -FilePath .\IPS.txt
