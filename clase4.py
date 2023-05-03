"""
A.union(B)
A.intersection(B)
A.difference(B)
A.symmetric_difference(B)
"""
def prodCart(X,Y):
    res = set()
    for x in X:
        for y in Y:
            res.add((x,y))
    return res

A = set(range(1,93))
def p1e27(A):
    A2 = prodCart(A, A)
    res = set()
    for (x,y) in A2:
        if ((x**2 - y**2) == (93*x - 93*y)):
            res.add((x,y))
    return res

def dominioNatural(R):
    res = set()
    for (x,y) in R:
        res.add(x)
    return res

def imagen(R):
    res = set()
    for (x,y) in R:
        res.add(y)
    return res
"""
auxiliar para esReflexiva
def inclusion(A,B):
    return A.union(B) == B

def esReflexiva(R):
    return dominioNatural(R).union(imagen(R)) == imagen(R)
creo q funciona bien, tomo la oficial por las dudas
"""
def esReflexiva(R):
    X = dominioNatural(R)
    for a in X:
        if not (a,a) in R:
            return False
    return True

def esAntiSimetrica(R):
    for (x,y) in R:
        if (y,x) in R and (y != x):
            return False
    return True
"""   
def esTransitiva(R):
    for (x,y) in R:
        for (y,z) in R:
            if ((y,z) in R) and (not (x,z) in R):
                return False
    return True
esta no funciona bien, no se porque
"""
def esTransitiva(R):
    for (x,y) in R:
        for (u,z) in R:
            if y == u:
                if not (x,z) in R:
                    return False
    return True

def esSimetrica(R):
    for (x,y) in R:
        if not (y,x) in R:
            return False
    return True

def esDeEquivalencia(R):
    return esTransitiva(R) and esSimetrica(R) and esReflexiva(R)

def claseDeEquivalencia(a,R):
    X = dominioNatural(R)
    res = set()
    for b in X:
        if (a,b) in R:
            res.add(b)
    return res

def clasesDeEquivalencia(R):
    X = dominioNatural(R)
    res = []
    for a in X:
        if claseDeEquivalencia(a,R) not in res:    
            res.append(claseDeEquivalencia(a,R))
    return res

X = set(range(10))
XxX = prodCart(X,X)
#R = set([(x,y) in XxX if (y-x) % 7 == 0])
#no funciona, sintaxis invalida
R = set()
for (x,y) in XxX:
    if (y-x) % 7 == 0:
        R.add((x,y))

#clasesDeEquivalencia(p1e27(A))

def esFuncion(R):
    return all([y == v for (x,y) in R for (u,v) in R if x == u])
    
def funcionARelacion(X,f):
    res = set()
    for x in X:
        res.add((x,f(x)))
    return res
def cubo(x):
    return x**3
cuboF = funcionARelacion(set(range(-3,3)),cubo)

def evaluar(F,x0):
    for (x,y) in F:
        if x == x0:
            return y

def preimagen(F,y0):
    res = set()    #conjunto vacio es "set()" y no "{}"
    for (x,y) in F:
        if y == y0:
            res.add(x)
    return res
#xt = {-3,-2,-1,0,1,2}
#def cuadrado(x):
#    return x**2
#cuadradoF = funcionARelacion(xt,cuadrado)

def esBiyectiva(F):
    return esFuncion(F) and esFuncion(inversa(F))
#auxiliar de esBiyectiva
def inversa(R): 
    res = set()
    for (x,y) in R:
        res.add((y,x))
    return res

def tuplaAFuncion(X,T):
    res = set()
    i = 0
    for x in X:
        res.add((x,T[i]))
        i = i + 1
    return res
"""
dato random, para construir tuplas de n elementos.
from itertools import product #creo q product es el prodCartesiano
Y = {0,1} # n=2
Ys = set(product(Y,repeat=3)) # construye YxYxY
"""
from itertools import product
def funciones(X,Y):
    Ys = set(product(Y,repeat=len(Y)))
    res = []
    for y in Ys:
        if esFuncion(tuplaAFuncion(X,y)):
            res.append(tuplaAFuncion(X,y))
    return res

xg = [1,2,3]
yg = [4,5,6]

def biyecciones(X,Y):
    Fs = funciones(X,Y)
    Bs = []
    for f in Fs:
        if esBiyectiva(f):
            Bs.append(f)
    return Bs

X = set(range(1,8))

def p3e14(X,Y):
    B = biyecciones(X, Y)
    res = []
    for b in B:
        if prodCart({1,2,3},{1,2}).intersection(b) == set():
            res.append(b)
    return res
#len(p3e14(X,X)) = 1440 = 5.4.3.4.3.2 (mi cuenta, creo q esta ok)


def partes(c):
    if len(c) == 0:
        return [[]]
    r = partes(c[:-1])
    return r + [s + [c[-1]] for s in r]
"""

"""


def powerset(fullset):
  listsub = list(fullset)
  subsets = []
  for i in range(2**len(listsub)):
    subset = []
    for k in range(len(listsub)):            
      if i & 1<<k:
        subset.append(listsub[k])
    subsets.append(subset)        
  return subsets
"""
no se que es "<<", supuestamente invierte los bits de un numero
binario. pero para eso tiene que estar bin().
"""

def addTo(e, t):       
        for s in t:
                s += [e]
        return t
 
def powerSet(a_set):
        if not a_set: return [[]]
        e = a_set[0]
        t = a_set[1:]
        return powerSet(t) + addTo(e, powerSet(t))
"""
saca el primer elemento y lo almacena en "e", el resto lo almacena
en "t". hace partes de "t", hace partes de "t" pero incluyendo al
elemento en "e", asi este pasa a estar en todos esos subconjuntos,
serian los subconjuntos donde esta ese primer elemento. luego une
esto con el resto de partes.
"""
"""
para partes usar funciones. hay una biyeccion entre funciones.
{0,1}**Y da funciones, en las que hay 1 pertenecen a partes.
"""
ej = [267,493,869,961,1000,1153,1246,1598,1766,1922]
def ej1(X):
    P = partes(X)
    for p in P:
        if sum(p) == 5842:
            return p
        
def ej2(n):
    A = partes(list(set(range(1,n+1)))) #debe haber algo mas corto
    idx = 0
    #u = []
    for a in A:
        if sum(a) % 5 == 0:
            idx = idx + 1
            #u.append(a)
    return idx #u
"""
relacion:
n / ej2
2 => 1
3 => 2
4 => 4
5 => 8
6 => 14
7 => 26
8 => 52
9 => 104
10 => 208
11 => 412
12 => 820
13 => 1640
14 => 3280
15 => 6560
16 => 13112
17 => 26216  #anomalia, no cumple
18 => 52432
19 => 104864
20 => 209728
21 => 419440
conjetura; parece que para n > 7, es el doble del anterior. cuando n es congruente a 1 mod 5 se rompe
el patron del a(n) = 2*a(n-1).
"""







 
    
    
    
