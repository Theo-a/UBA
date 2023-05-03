def CeroFT(f,f_prima,x_0):
    p = f(x_0)
    m = f_prima(x_0)
    return (-p)/m + x_0
"""
0 = m(x-x_0) + p
x = (-p)/m + x_0
"""
def cuadratica(x):
    return x**2
def cuadratica_prima(x):
    return 2*x

def NR(f,f_prima,x_0,tol):
    idx = x_0
    while abs(f(idx)) >= tol:
        idx = CeroFT(f,f_prima,idx)
    return idx  
#CeroFT(f,f_prima,idx) en abs(f(idx))

def g(x):
    return x**3 - 2*x - 5
def g_p(x):
    return 3*(x**2) - 2
dom_g = [0,1,2,3]

import math
def h(x):
    return x - 1 - 0.5*math.sin(x)
def h_p(x):
    return 1 -0.5*math.cos(x)
dom_h = [0,1,2]

def l(x):
    return (x+1)*math.exp(x) - 4
#math.exp() es "e" a la "x"
def l_p(x):
    return math.exp(x) + (x+1)*math.exp(x)

import matplotlib.pyplot as plt
import numpy as np
#no.arrange() para hacer lista con float

def plot_fun(f,dom):
    xs = dom
    ys = []
    for x in dom:
        ys.append(f(x))
    plt.plot(xs,ys)
"""
def biseccion1(fun,a,b,e):
    while b-a > e:
        c = (a+b)/2
        if fun(c) == 0:
            return c
        if fun(a)*fun(c) < 0:
            b = c
        else:
            a = c
        return c
"""    


#derivada mala,hace cociente incremental con h dado.        
#def deriv(f,x_0,h):
def suma_hasta_n(n):
    suma = 0
    for i in range(1,n):
        suma = suma + i
    return suma

def suma_primeros_naturales(n):
    valor = 0
    i = 1
    while i <= n: 
        valor = valor + i
        i = i + 1
    return valor
    
"""
parcial:
    parte con lapiz y papel, como en los cuestionarios de la
    pag. mas teorico.
    parte programacion, 2 ejs, no tan dificiles.
    hay un machete en el campus.
"""
    

   
