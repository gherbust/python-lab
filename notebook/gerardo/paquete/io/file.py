import os

def openFile(path):
    f = open(path,encoding="utf-8")

    lines = f.readlines()
    print(lines)
    for l in lines:
        print(l)

    if not f.closed:
        f.close()
# todo: guardado de archivos pendiente
        
def saveFile(file_path,lista):
    file = os.open(file_path, os.O_RDWR|os.O_CREAT)

    lineas = ""

    for i in lista:
        lineas += str(i)+"\n"
    txt = str.encode(lineas)
    totalBytes = os.write(file,txt)
    os.close(file)
    print(totalBytes)
