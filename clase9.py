def minimoUnimodal(a,b,phi,k_max,e):
    k = 0
    a_k = a
    b_k = b
    while abs(b_k - a_k) > e or k < k_max:
        k = k + 1
        if phi((3*a_k + b_k)/4) < phi((a_k + 3*b_k)/4):
            a_k = a_k
            b_k = (a_k + 3*b_k)/4
        else:
            a_k = (3*a_k + b_k)/4
            b_k = b_k
    return (b_k + a_k)/2

import math

def phi1(t):
    return abs(t-2)
def phi2(t):
    return t**2 - 3*t + 1
def phi3(t):
    return t*math.log(t)

import matplotlib.pyplot as plt
def plot(f,a,b): #funcion auxiliar
   X = [i for i in range(a,b)]
   Y = []
   for x in X:
       Y.append(f(x))
   plt.plot(X,Y)
# minimoUnimodal(0,4,phi1,20,0.5) => 1.999...
# minimoUnimodal(-2,4,phi2,20,0.5) => 1.502...
# minimoUnimodal(1,3,phi2,20,0.5) => 1.499...
# minimoUnimodal(1,3,phi2,20,0.5) => 1.499...

def derivadNum(g,t,h,metodo):
    if metodo == "centrada":
        return (g(t+h)-g(t-h))/(2*h)
    return (g(t+h)-g(t))/h

def g(x):
    return x**3

G = []

for k in range(1,21):
    G.append(derivadNum(g, 5, 1/(10**k), 0))
#plt.plot([i for i in range(1,21)],G)

def derivadNum2(g,t,metodo):
    if metodo == "centrada":
        return (g(t + 10**(-5))-g(t - 10**(-5)))/(2*(10**(-5)))
    return (g(t + 10**(-5))- g(10**(-5)))/(10**(-5))

import numpy as np

def derivada_parcial_i(f,x,i):
    e_i = [0]*len(x)
    e_i[i] = 1
    e_i = np.array(e_i)
    
    h = 1e-5 #1*10**(-5)
    
    return (f(x+h*e_i)-f(x))/h

def gradiente(f,x):
    lista_deriv_parc = []
    for i in range(len(x)):
        lista_deriv_parc.append(derivada_parcial_i(f,x,i))
    return np.array(lista_deriv_parc)

def descensGradiente(f,x0,k_max,e):
     







