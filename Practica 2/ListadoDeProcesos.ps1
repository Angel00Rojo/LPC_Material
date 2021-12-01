$ps = Get-Process
for($i=0;$i -lt $ps.Length; $i=$i+5){
    Write-Output $ps[$i].Name
}
