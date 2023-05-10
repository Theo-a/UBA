"terea que no hice ni entregué"
def f(x):
    if x % 2 == 0:
        return x/2
    if x == 1:
        return x
    elif x % 2 != 0:
        return 3*x + 1
    
"""
def largo(n):
    a = n
    idx = 0
    while a != 1:
        a = f(n)
        idx = idx + 1
    return idx
no funciona, porq?
"""
def largo(n):
    idx = 1
    while n != 1:
        n = f(n)
        idx = idx + 1
    return idx

def lists(n):
    res = [n]
    while n != 1:
        n = f(n)
        res.append(n)
    return len(res)

def c(n):
    for i in range(n):
        u = 1
        if f(i) > u:
            u = f(i)
    return u
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
