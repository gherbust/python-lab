def suma(a,b) -> int:
    return a+b

def resta(a,b) ->int:
    return a-b

def fibo(n)->None:
    a,b= 0,1
    while a<n:
        print(a,end= ' ')
        a,b = b, a+b
    print()

