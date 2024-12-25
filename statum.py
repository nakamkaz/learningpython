import math

def expected (ax,ap):
    ep=0
    for i in range(len(ax)):
        ep += ax[i] * ap[i]
    return ep

def variance(ax,ap):
    vx = 0
    em = expected (ax,ap)
    for i in range(len(ax)):
        vx += ( (ax[i] - em)**2 ) * ap[i]
    return vx

def variance0 (ax,ap):
    vx0 = 0
    em = expected(ax,ap)
    for i in range(len(ax)):
        vx0 += (ax[i]**2 ) * ap[i]
    return vx0 - em**2 

def std(ax,ap):
    return math.sqrt(variance(ax,ap))

hx = [1,2,3,4,5,6]
hp = [1/6,1/6,1/6,1/6,1/6,1/6]

print ("E(X)  ", expected(hx,hp))
print ("v(X)  ", variance(hx,hp))
print ("V(X)0 ", variance0(hx,hp))
print ("std   ", std(hx,hp))
print ("std 0 ", math.sqrt(variance0(hx,hp)))
