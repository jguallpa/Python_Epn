#funcion que recibe un parametro(n) y crea los numeros de la sucesión Fibonacci 

def fibo(Num):
    if(Num == 0):
        return 0
    elif(Num == 1):
        return 1
    else:
        return (fibo(Num - 1) + fibo(Num - 2))

def fibo_prof(n):
    a, b=0,1
    while a<=n:
        print(a, end='')
        c=a+b
        a=b
        b=c
    print()
    

    
    
def a():
    pass

def b():
    pass
