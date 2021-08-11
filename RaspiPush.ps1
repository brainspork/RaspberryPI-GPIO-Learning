$envJson = Get-Content './excluded/env.json' | Out-String | ConvertFrom-Json

# name of the raspberry pi
$name = $envJson.name
# path to the folder to copy to
$root = $envJson.root
$pathToSSH = $envJson.pathToSSH

# TODO: some kind of settings json of the black and white lists

$cmd = "rsync -av -e " + $pathToSSH +"ssh.exe --include='*.py' --exclude='*.*' --exclude='excluded' --exclude='.vscode' . " + $name + ":" + $root

Write-Output $cmd

Invoke-Command -ScriptBlock {((bash -c $cmd) | Out-String)}