def armonica(n):
    suma = 0
    div = n
    while div >= 1:
        suma = suma + 1/div
        div = div - 1
    return suma

def factorial(n):
    ind = n
    prod = n
    resul = n
    while ind > 2:
        resul = resul*(prod-1)
        prod = prod - 1
        ind = ind -1
    if n == 2:
        return 1
    return resul

"""
Formas de crear listas (con 100 elementos ahora)
asW = []
n = 1
while len(asW) < 100:
    asW.append(armonica(n))
    n = n+1
    
asF = []
for i in range(1,101):
    asF.append(armonica(n))

asFC = [armonica(n) for i in range(1,101)]
dice que n no esta definido(?)
"""

asW = []
n = 1
while len(asW) < 100:
    asW.append(armonica(n))
    n = n+1
    
import matplotlib.pyplot as plt
from math import log
"""
xs = []; arms = []; logs = []
for n in range(10,100):
    xs.append(n)
    arms.append(armonica(n))
    logs.append(log(n))
plt.scatter(xs,arms,color='red');\
    plt.plot(xs,logs)
"""
def alInfinito(n):
    ind = n
    while armonica(ind) < n:
        ind = ind + 1
    return ind
        
from math import cos
"""
xs = []; ys = []
for n in range(1,1000):
    xs.append(n)
    ys.append(cos(n))
plt.scatter(xs,ys)    
"""
Cn = []
for i in range(1000):
    Cn.append(cos(i))

Cnpos = []
for i in range(n):
    c = Cn[i]
    if c > 0:
        Cnpos.append(c)
# Cnpos = [c for c in Cn if c > 0]
     

def cosCerca1(n0,n1,e):
    resul = []
    for n in range(Cnpos):
        if n0 < n < n1 and (cos(n) > 1-e):
            resul.append(n)
    return resul
#no esta cheuqueada, no se como

def cosTiendeA1(k):
    resul = []
    for i in range(1,k+1):
        if cos(i) > 1 - 1/i:
            resul.append(i)
    return resul
    
modCn = [abs(c) for c in Cn]
#lista con modulos de Cn, abs es la funcion modulo de python  

def alInfinito2(fun,r):
    n = 1
    an = fun(1)
    while an < r:
        n = n+1
        an = fun(n)
    return n
#toma como parametro "fun" a funciones

def sumaParcial(an,n):
    suma = 0
    for i in range(n):
        suma = suma + an[i]
    return suma
"""
biseccion que devuelve los n intervalos [a,b]
def biseccion(fun,a,b,n):
    a1 = a
    b1 = b
    c = (a1 + b1)/2
    nmax = [(a,b)]
    for i in range(n):
        if (fun(a1)*fun(b1) < 0) and (fun(a1)*fun(c) < 0):
            b1 = c
            nmax.append((a1,b1))
        else:
            a1 = c
            nmax.append((a1,b1))
    return nmax
  
biseccion que devuelve el n-esimo intervalo [a,b]
def biseccion(fun,a,b,n):
    a1 = a
    b1 = b
    c = (a1 + b1)/2
    for i in range(n):
        if (fun(a1)*fun(b1) < 0) and (fun(a1)*fun(c) < 0):
            b1 = c
        else:
            a1 = c
    return [a1,b1]
 """  
    
    
    
    
    
    
  