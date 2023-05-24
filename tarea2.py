def mcd(a,b):
    if min(a,b) == 0:
        return max(a,b)
    if min(a,b) == 1:
        return 1
    while min(a,b) != 0 and min(a,b) != 1:
        a = max(a,b)%min(a,b)
        b = min(a,b)

def mcm(a,b):
    return (a*b)//mcd2(a,b)


def mcd2(a,b):
    div_com = []
    for i in lis_divs(a):
        if i in lis_divs(b):
            div_com.append(i)
    mcd = 0
    for k in div_com:
        if k > mcd:
            mcd = k
    return mcd    
def lis_divs(n):
    Divs = []
    for i in range(1,n+1):
        if n%i == 0:
            Divs.append(i)
    return Divs

def sonCoprimos(a,b):
    return mcd2(a,b) == 1