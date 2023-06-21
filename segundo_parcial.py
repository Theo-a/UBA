prueba_x=[10,11,12,13,14,15,16,17,18,19,20]
prueba_y=[19.87,27.54,40.74,50.72,62.97,87.40,118.28,169.06,223.18,294.71,398.58]

# 1).

import matplotlib.pyplot as plt

#plt.scatter(prueba_x,prueba_y)

# 2).

import math

def error_cuadratico_con_exponencial(lista_x,lista_y,tita):
    suma = 0
    for i in range(len(lista_y)):
        suma = suma + (lista_y[i] - math.exp(tita*lista_x[i]))**2
    return suma

# 3).

# tita = 0.25 => f = 130403.3594
# tita = 0.5 => f = 735871477.5277
# tita = 0.75 => f = 13751792902465.387
    
# yo eligirìa tita = 0.25
    
# 4).

def exponencial(x):
    return math.exp(0.25*x)

Xs = [k for k in range(10,21)]
Ys = []
for i in range(len(Xs)):
    Ys.append(exponencial(i))
#plt.plot(Xs,Ys)
#plt.scatter(prueba_x,prueba_y)

# 5).

def grilla(a,b,paso):
    grilla = [a]
    ai = a
    while ai < b:
        grilla.append(ai)
        ai = ai + paso
    grilla.append(b)
    return grilla
           
def mejor_exponencial(lista_x,lista_y,a,b,paso):
    Gr = grilla(a,b,paso)
    minimo = error_cuadratico_con_exponencial(lista_x,lista_y,Gr[0])
    indx = Gr[0]
    for i in Gr:
        if error_cuadratico_con_exponencial(lista_x,lista_y,i) < minimo:
            minimo = error_cuadratico_con_exponencial(lista_x,lista_y,i)
            indx = i
    return indx

# 6).¨
    
A = mejor_exponencial(prueba_x,prueba_y,0,1,0.01) #0.3000000000000001

# 7).

X = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]
Y = [20.08, 36.56, 34.86, 43.05, 70.29, 88.25, 116.68, 158.07, 223.57, 297.09, 402.84 ]

a = error_cuadratico_con_exponencial(X,Y,0.3)
#215.68197436863238
    
b = mejor_exponencial(X,Y,0,1,0.025)
# 0.3
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
