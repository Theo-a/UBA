# cosas de clase pasada y tarea
"""
def mcd(a,b):
    x = a
    y = b
    while y != 0: # while y: y igual a 0 es un Flase, osea
        #se lee como un booleano
        r = x%y
        x = y
        y = r
    return x
    
def mcd2(a,b):
    c = a%b
    while c: # while y: y igual a 0 es un Flase, osea
        #se lee como un booleano
        a = b
        b = c
        c = a%b
    return a

def mce3(a,b):
    mcd = 1
    i = 2
    while i <= a and :
        #lo van a subir
        
"""        

#ver funcion dict,toma una lista con tuplas y las hace 
#diccionario
#dict[key] = value cambiar el valor si ya existe la key, y si no
#crea una con ese valor
#dict.keys() devuele una lista con las keys.



#de clase 6
def pol_lagrange(Xs,Ys,x):
    Pn = 0
    for i in range(len(Xs)):
        js = [k for k in range(len(Xs))]
        js.remove(i)
        li = 1
        for j in js:
            li = li*(x-Xs[j])/(Xs[i]-Xs[j])
        Pn = Pn + Ys[i]*li
    return Pn


#sacado de clase 3
def construir_grilla(a,b,paso):
    grilla = []
    i = a
    while i < b:
        grilla.append(i)
        i = i + paso
    grilla.append(b)
    return grilla
#arrgelar para que de n+1 y no n+2 en len de lista, es por
#es por error de redondeo
def construir_grilla2(a,b,paso,n):
    # n longitud de las lista (es n+1)
    grilla = []
    i = a
    while len(grilla) < n:
        grilla.append(i)
        i = i + paso
    grilla.append(b)
    return grilla

def interpolando_lagrange(f,a,b,n,x_eval):
    #x_lis = [i for i in range(a,b,(b-a)/n)] creo que con np.arrange funciona
    x_lis = construir_grilla2(a,b,(b-a)/n,n)
    y_lis = []
    for i in range(len(x_lis)):
        y_lis.append(f(x_lis[i]))
    return pol_lagrange(x_lis,y_lis,x_eval)

def f1(x):
    return 1/(1 + 25*(x**2))

import math
def f2(x):
    return math.sin(math.pi*x)

import matplotlib.pyplot as plt

def plot(f,n):
    Xs = construir_grilla2(-1,1,(1-(-1))/n,n)
    Ys = []
    for i in range(len(Xs)):
        Ys.append(interpolando_lagrange(f,-1,1,n,Xs[i]))
    return plt.plot(Xs,Ys)
#hacer que plotee la funcion y lagrange superpuesto, y usar
#scatter para mostrar las interpolaciones
    
def plot2(f,n):
    Xs = construir_grilla2(-1,1,(1-(-1))/n,n)
    Ys = []
    for i in range(len(Xs)):
        Ys.append(interpolando_lagrange(f,-1,1,n,Xs[i]))
    Ys2 = []
    for k in range(len(Xs)):
        Ys2.append(f(k))
    plt.plot(Xs,Ys2)
    return plt.plot(Xs,Ys)

#de tarea 2
    
def mcd2(a,b):
    div_com = []
    for i in lis_divs(a):
        if i in lis_divs(b):
            div_com.append(i)
    mcd = 0
    for k in div_com:
        if k > mcd:
            mcd = k
    return mcd
def lis_divs(n):
    Divs = []
    for i in range(1,n+1):
        if n%i == 0:
            Divs.append(i)
    return Divs
def mcm(a,b):
    return (a*b)//mcd2(a,b)

def posibles_pares(D,M):
    lis = []
    for i in range(D*M):
        for j in range(D*M):
            if mcd2(i,j) == D and mcm(i,j) == M:
                lis.append((i,j))
    return lis
#usar otra fun mcd mas corta y facil

def mcd_max(n):
    lis = []
    for i in range(1,n-1):
        for j in range(1,n):
            lis.append(mcd2(i,j))
    res = 0
    for k in lis:
        if k > res:
            res = k
    return res

def es_perfecto(n):
    return sum(lis_divs(n)) == 2*n

# de clase 4
def partes(c):
    if len(c) == 0:
        return [[]]
    r = partes(c[:-1])
    return r + [s + [c[-1]] for s in r]    

def es_practico(n):
    sumas_posibles = []
    for k in sumas_partes(lis_divs(n)):
        if k <= n:
            sumas_posibles.append(k)
    lis = set()
    for d in lis_divs(n):
        for s in sumas_posibles:
            if d == s:
                lis.add(s)
    return len(lis) == len(lis_divs(n))
#hay valores repetidos en lis, uso sets

#falta hacer la suma de los conj de partes, tmb hay sumas
#posibles que nunca pueden ser usadas.

def sumas_partes(n):
    r = []
    for i in partes(n):
        r.append(sum(i))
    return r




























