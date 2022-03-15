$ie=New-Object -ComObject "internetexplorer.Application"
$ie.Visible = $true

Start-Sleep -Seconds 8
$ie.Navigate("https://www.facebook.com/")

while($ie.busy -eq $true)
{
Start-Sleep -Seconds 1
Write-Host "loading the console...... please wait..."
}
Start-Sleep -Seconds 10
$username = $ie.Document.IHTMLDocument3_getElementById('email')
$username.value="**************************************************************"
$password = $ie.Document.IHTMLDocument3_getElementById('pass')
$password.value="******************"
$ie.Document.IHTMLDocument3_getElementById('u_0_b').click()
