import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import math
"""
X,Y,Z = [0,1,2],[1,1,1],[1,2,3]
ax = plt.axes(projection='3d')
ax.scatter3D(X,Y,Z, color = 'r')
plt.show()
"""

X,Y = np.linspace(-5,5,1000),np.linspace(-5,5,1000)
X, Y = np.meshgrid(X, Y) #interpreta a X,Y como un objeto bidimensional(?
Z = X**2+Y**2
"""
ax = plt.axes(projection='3d')
ax.plot_surface(X,Y,Z)
ax.view_init(60, 35) #cambia punto de vista
plt.show()
"""

""" grafico de nivel
ax = plt.axes(projection='3d')
ax.contour(X, Y, Z, 20, cmap='plasma')
plt.show()
"""

""" los mismo pero visto desde arriba
ax = plt.axes(projection='3d')
ax.contour(X, Y, Z, 20, cmap='plasma')
ax.view_init(90,90)
plt.show()
"""

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-6, 6, 100)
y = np.linspace(-6, 6, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
""" coloreado de violeta
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap=
'Purples')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
"""

def f1(x,y):
    return x**2 + 25*(y**2)

def f2(x,y):
    return x**2 + y**2 + (0.5*x + y)**2 + (0.5*x + y)**2

def f3(x,y):
    return (4 - 2.1*(x**2) + (1/3)*(x**4))*(x**2) + x*y + (-4 - 4*(y**2))*(y**2)
"""
x1 = np.linspace(-3, 3, 100)
y1 = np.linspace(-3, 3, 100)
X1, Y1 = np.meshgrid(x, y)
Z1 = f3(X, Y)
ax = plt.axes(projection='3d')
ax.contour3D(X1, Y1, Z1, 50, cmap='Purples')
plt.show()
"""

def f4(x,y):
    return 0.5*(x-4.5)**2 + 2.5*(y-2.3)**2


def norma2(x):
    R = 0
    for i in range(len(x)):
        R = R + x[i]**2
    return math.sqrt(R)

def descenso_gradiente(f, x, tol, n_iter, paso):
    iteraciones = 0
    x1 = x - paso * gradiente(f,x)
    lista_x = [x[0]]
    lista_y = [x[1]]
    lista_z = [f(x)]
    while norma2(x1-x) > tol and iteraciones < n_iter:
        x = x1
        lista_x.append(x[0])
        lista_y.append(x[1])
        lista_z.append(f(x))
        
        x1 = x - paso * gradiente(f,x)
        
        iteraciones = iteraciones + 1
        
    return [lista_x, lista_y, lista_z, iteraciones]
    
def gradiente(f,x):
    lista_deriv_parc = []
    for i in range(len(x)):
        lista_deriv_parc.append(derivada_parcial_i(f,x,i))
    return np.array(lista_deriv_parc)

def derivada_parcial_i(f,x,i):
    e_i = [0]*len(x)
    e_i[i] = 1
    e_i = np.array(e_i)
    
    h = 1e-5 #1*10**(-5)
    
    return (f(x+h*e_i)-f(x))/h 
    
    
    
    
    
    
    
    
    
    
    
    
    