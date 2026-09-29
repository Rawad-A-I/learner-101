# Registers a per-user logon task that starts the listener hidden. Run once:
#   powershell -ExecutionPolicy Bypass -File scripts\install_autostart.ps1
# Remove with: Unregister-ScheduledTask -TaskName Learner101Listener -Confirm:$false
$root = Split-Path -Parent $PSScriptRoot
$python = (Get-Command pythonw.exe -ErrorAction Stop).Source
$action = New-ScheduledTaskAction -Execute $python -Argument "`"$root\listener\listener.py`"" -WorkingDirectory $root
$trigger = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit ([TimeSpan]::Zero) -RestartCount 3 -RestartInterval (New-TimeSpan -Minutes 1)
Register-ScheduledTask -TaskName Learner101Listener -Action $action -Trigger $trigger -Settings $settings -Description "Learner 101 webhook listener + ngrok tunnel" -Force | Out-Null
Write-Host "Registered Learner101Listener; it starts at next logon. Start now with: Start-ScheduledTask Learner101Listener"
