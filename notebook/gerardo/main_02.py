from paquete.mat.opera import *
from paquete.io.file import *
from paquete.io.rest_client import *
import os


openFile("C:/Users/gherb/curso/python-lab/notebook/gerardo/file.txt")
#resta()
#suma()

print(dir())

lista = [5,'dsds',"sdsdsd",1,2,5,8965,498,687,None," ",546,5,2546,54]
try:
    saveFile("C:/Users/gherb/curso/python-lab/notebook/gerardo/nuevo.txt",lista)
except Exception as e:
    print("no guardo")
finally:
    print("enviar correo")



try:
    f = open("C:/Users/gherb/curso/python-lab/notebook/gerardo/nuevo.txt") 
    s = f.readline()
    i = int(s.strip())
except FileNotFoundError as oError:
    print("Error del os:", oError)
except OSError as oError:
    print("Error del os:", oError)
except NameError as vError:
    print("Error en el valor File:", vError)
except Exception as ex:
    print("Error no controlado")



try:
    openFile()
except Exception as ex:
    print("Error al abrir archivo: ",ex)
