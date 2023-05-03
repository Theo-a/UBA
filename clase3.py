#grilla = [i for i in range(-3,3,0.01)]
#no funciona range() con floats, si o si int
grilla = []
n = -3
while n < 3:
    grilla.append(n)
    n = n + 0.01
def cuadratica(x):
    return x**2
grilla2 = [cuadratica(x) for x in grilla]
#plt.plot(grilla,grilla2)   
import matplotlib.pyplot as plt
def plotFun(lis, fun):
    xs = [fun(x) for x in lis]
    plt.plot(lis, xs)
    
def construir_grilla(a,b,paso):
    grilla = []
    i = a
    while i < b:
        grilla.append(i)
        i = i + paso
    grilla.append(b)
    return grilla

def f(x):
    if x <= -1:
        y = x + 2
    elif -1 < x <= 1:
        y = -x
    else:
        y = 3*x-4
    return y
#plotFun(construir_grilla(-10,10,0.2),f)

def g(x):
    if x <= -4:
        y = 3*x+1
    else:
        y = 1/(x+2)
    return y
#plotFun(construir_grilla(-5,5,0.1),g)

def p(x):
    return (x**5 - 11*(x**3) +14*(x**2) - 2)
#plotFun(construir_grilla(-10,10,0.2),p)


def biseccion(fun,a,b,e):
    while b-a > e:
        c = (a+b)/2
        if fun(c) == 0:
            return c
        if fun(a)*fun(c) < 0:
            b = c
        else:
            a = c
        return c

#faltan hacer ej 4,5,6
            
            
            
        
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
