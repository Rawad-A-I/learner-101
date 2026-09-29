# Starts the Learner 101 listener and its ngrok tunnel in this window.
Set-Location -Path $PSScriptRoot
python listener\listener.py @args
