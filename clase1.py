"Taller de Programación"

import random

def cuantas_figus(figus_total):
    album = [0]*figus_total
    cantidad = 0
    #while sum(album) < nro_figus:
    while not all (album):
        figurita = random.randint(0, figus_total-1)
        album[figurita] = 1
        cantidad = cantidad+1
    return cantidad

def promedio(lista):
    return (sum(lista)/len(lista))

def simular_muchas_repeticiones(n_rep, figus_total):
    lista_rep = []
    for i in range(n_rep):
        lista_rep.append(cuantas_figus(figus_total))
    return lista_rep
#promedio(simular_muchas_repeticiones(1000,6)) 14.793
#promedio(simular_muchas_repeticiones(1000,12)) 37.326
#cuantas_figus(638) 5382
def cantidad_figus_esperadas(figus_total):
    div = 0
    resul = 0
    for i in range(figus_total):
        div = div+1
        resul = resul + (figus_total/div)
    return resul

import matplotlib.pyplot as plt

xs = [6,7,8,9,10]
ys = [14.7,18.15,21.74,25.46,29.28]
#plt.plot(x,y) plt.plot(x,y,"o")
#usar !pip install matplotlib
plt.plot(xs,ys)
plt.show()

