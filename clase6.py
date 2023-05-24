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

xs = [8,9,14,17,18,19,20.5,21.5,23,24,25,26]
ys = [264,285,346,417,438,495,524,540,643,693,744,780]

import matplotlib.pyplot as plt

#plt.plot(xs,ys)

def lis_divs(n):
    Divs = []
    for i in range(2,n+1):  #usar (n+1)/2 ?
        if n%i == 0:
            Divs.append(i)
    return Divs
    
def es_primo(n):    
    return lis_divs(n) == [n]
    
def div_hasta_n(n):
    dic = {}
    for i in range(1,n+1):
        dic[i] = lis_divs(i)
    return dic
    
def primos_hasta_n(n):
    primos = []
    for i in range(1,n+1):
        if es_primo(i):
            primos.append(i)
    return primos

def factorizacion(n):
    dic = {}
    for i in primos_hasta_n(n):
        dic[i] = 0
    while n > 1:
        for d in primos_hasta_n(n):
            if n%d == 0:
                dic[d] += 1
                n = n//d
    return dic
                
    
            
    
    
    
    
    
    
    
    
    
    