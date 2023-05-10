# 1).
    # a).
def serie(n):
        suma = 0
        for i in range(1,n+1):
            suma = suma + 1/(i*(i+1))
        return suma
    
    # b).
    # n = 3, Sn = 0.75
        
    # c).
import matplotlib.pyplot as plt
def grafico(n):
        xs = []
        for i in range(1,n+1):
            if i%2 == 0:
                xs.append(i)
        ys = []
        for u in xs:
            ys.append(serie(u))
        return plt.plot(xs,ys)
    #grafico(100)
        
    # d).
def n_cero(e):
        n = 1
        while abs(serie(n)-1) >= e:
            n = n + 1
        
        return n
    # e).
    # n = 1/30, n_cero(1/30) = 30
    
# 2).
    # a).
def esDensa(X,R):
        for (x,y) in R:
            for z in X:
                if (not((x,z) in R)) or (not((y,z) in R)):
                    return False
        return True
                    
    # b).
def prodCart(X,Y):  #funcion auxliar
    res = set()
    for x in X:
        for y in Y:
            res.add((x,y))
    return res

def relacion(X):
    C = prodCart(X,X)
    R = set()
    for (x,y) in C:
        if ((x + 2*y) % 303) == 0:
            R.add((x,y))
    return R
            
X = []    
for i in range(1,201):
    X.append(i)
#relacion(X)
#esDensa(X,relacion(X)) -> False


        












