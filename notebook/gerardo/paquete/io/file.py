def openFile(path):
    f = open(path,encoding="utf-8")

    lines = f.readlines()
    print(lines)
    for l in lines:
        print(l)

    if not f.closed:
        f.close()
# todo: guardado de archivos pendiente
