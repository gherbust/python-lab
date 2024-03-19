from modulos.operaciones import *
'''import modulos.opera as o
import modulos.operaciones as op

o.resta(4,5)
o.fibo(10)

op.resta(4,5)
op.suma(4,5)

fibo(10)'''

print('Selecciona una opcion: \n')
print('opcion 1 suma: \n')
print('opcion 2 resta: \n')
print('opcion 3 Fibonacci: \n')

opcion = input()

match opcion:
    case '1':
        print("valor de a: \n")
        a=input()
        print("valor de b: \n")
        b=input()
        r=suma(int(a),int(b))
        print("resultado: ",r)
    case '2':
        print("valor de a: \n")
        a=input()
        print("valor de b: \n")
        b=input()
        r=resta(int(a),int(b))
        print("resultado: ",r)
    case '3':
        print("valor de n: \n")
        a=input()
        fibo(int(a))
    case _:
        print("Opcion incorrecta!!")
