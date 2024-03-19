from paquete.mat.opera import *
from paquete.io.file import *
from paquete.io.rest_client import *
import json

openFile("C:/Users/gherb/curso/python-lab/notebook/gerardo/file.txt")
#resta()
#suma()

print(dir())

lista = [5,'dsds',"sdsdsd",1,2,5,8965,498,687,None," ",546,5,2546,54]

saveFile("C:/Users/gherb/curso/python-lab/notebook/gerardo/nuevo.txt",lista)


client = restclient("https://jsonplaceholder.typicode.com/todos")
txt = client.get()
print(txt)

data = json.loads(txt)
print(type(data))
delim=","
row = ["id","user id","title","completed"]
string_builder = delim.join(row)+ "\n"
for dato in data:
    #string_builder += str(dato['userId'])+","+dato['title']+","+ str(dato["completed"])+"\n"
    #string_builder += "{0},{1},{2}\n".format(str(dato['userId']),dato['title'],str(dato["completed"]))
    #string_builder += "{userId},{title},{completed}\n".format(title=dato['title'],userId=str(dato['userId']),completed=str(dato["completed"]))
    string_builder += "{id},{userId},{title},{completed}\n".format(**dato)

file = os.open("C:/Users/gherb/curso/python-lab/notebook/gerardo/todos.txt", os.O_RDWR|os.O_CREAT)
txt = str.encode(string_builder)
os.write(file,txt)
os.close(file)


    
