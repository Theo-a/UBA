prueba_x=[8,9,14,17,18,19,20.5,21.5,23,24,25,26]
prueba_y=[264,285,346,417,438,495,524,540,643,693,744,780]

import matplotlib.pyplot as plt
#plt.scatter(prueba_x,prueba_y)

def error_cuadratico_con_constante(lista_y,c):
    L = 0
    for y in lista_y:
        L = L + (y-c)**2
    return L
"""
.200 => 1515605
.400 => 488005
.600 => 420405
"""
"""
plt.scatter(prueba_x,prueba_y,color="black")
plt.axhline(y=200,color="green")
plt.axhline(y=400,color="blue")
plt.axhline(y=600,color="red")
"""
"""
calcular analiticamente, es hacer la derivada a mano
2*(x_i - c)*(-1) => -2*sum(prueba_x) == -2*c*n => c == sum(prueba_x)/len(prueba_x)
c = promedio
"""
"""
def L_prima(c):
    L = 0
    for i in prueba_x:
        L = L + 2*(i-c)
    return L
Ys = []
for i in prueba_x:
    Ys.append(L_prima(i))
plt.plot(prueba_x,Ys)
"""

def promedio(lis):
    suma = 0
    for i in lis:
        suma = suma + i
    return suma/len(lis)
#promedio(prueba_y) => 514.0833333333334

def error_cuadratico_con_recta(lista_x,lista_y,a,b):
    L = 0
    for i in range(len(lista_y)):
        L = L + (lista_y[i] - (a + b*lista_x[i]))**2
    return L
"""
.(-220,35) => 114012.5
.(-180,37) => 53188.5
.(-185,34) => 82045.0
"""

"""
calcular analiticamente el de recta,derivadas parciales
Da = 2*(y_i - a + b*x_i)*(-1) == 0
Db = 2*(y_i - a + b*x_i)*(x_i) == 0
=>
a == y_i + b*x_i
b == ((a-y_i)*x_i)/(x_i**2)
a => b
b == ((b*x_i)*x_i)/(x_i**2)
"""

"""
import pandas as pd
datos = pd.read_csv("lagrange_clase06.csv",sep
= ';',decimal=",")
"""
"""
dataframe
datos["x"] => devuelve columna con x, valores de lista x
lista(datos["x"]) => lista x
"""

def mejor_recta(lista_x,lista_y):
    X = promedio(lista_x)
    Y = promedio(lista_y)
    B = 0
    D = 0
    for i in range(len(lista_x)):
        B = B + ((lista_x[i] - X)*(lista_y[i] - Y))
    for i in range(len(lista_x)):
         D = D + ((lista_x[i] - X)**2)
    return [Y-(B/D)*X,B/D]
# error_cuadratico_con_recta(prueba_x,prueba_y,-5405.31030372784, 315.7009939765959)
# =>  31807042.727032732
    
def predigo_con_recta(lista_x,lista_y,x_nuevo):
    A = mejor_recta(lista_x,lista_y)
    return A[0] + A[1]*x_nuevo
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        