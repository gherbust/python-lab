import os

def openFile(path=""):
    try:
        if len(path) ==0 :
            raise FileNotFoundError("ruta del archivo vacia")
        f = open(path,encoding="utf-8")

        lines = f.readlines()
        print(lines)
        for l in lines:
            print(l)

        if not f.closed:
            f.close()
    except FileNotFoundError as ex:
        raise ex
    except Exception as ex:
        raise ex
    # todo: guardado de archivos pendiente
        
def saveFile(file_path,lista):
    try:
        file = os.open(file_path, os.O_RDWR|os.O_CREAT)

        lineas = ""

        for i in lista:
            lineas += str(i)+"\n"
        txt = str.encode(lineas)
        totalBytes = os.write(file,txt)
        os.close(file)
        print(totalBytes)
    except Exception as ex:
       raise ex
        