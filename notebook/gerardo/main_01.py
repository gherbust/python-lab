from paquete.mat.opera import *
from paquete.io.file import *
from paquete.io.rest_client import *

openFile("C:/Users/gherb/curso/python-lab/notebook/gerardo/file.txt")
#resta()
#suma()

print(dir())

lista = [5,'dsds',"sdsdsd",1,2,5,8965,498,687,None," ",546,5,2546,54]

saveFile("C:/Users/gherb/curso/python-lab/notebook/gerardo/nuevo.txt",lista)


client = restclient("https://jsonplaceholder.typicode.com/todos")
txt = client.get()
print(txt)