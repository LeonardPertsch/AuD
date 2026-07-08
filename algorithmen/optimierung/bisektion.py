"""
Bisektionsverfahren
===================

Findet eine Nullstelle von f, indem das Intervall [a, b] wiederholt
halbiert wird. Voraussetzung: f(a) und f(b) haben verschiedene Vorzeichen.

Laufzeit: O(log((b-a)/genauigkeit))
"""

def fn(x):
    return x**3+x**2-x

def bisection(a,b,accuracy):

    c = (a+b)/2
    while abs(a-b)>accuracy:
        if (fn(c) *fn(a)) <0:
            b = c
        else:
            if fn(c)*fn(b)<0:
                a=c
            else:
                return c
        c=(a+b)/2
    return c
print(bisection(-20,5,0.000000000001))

#geht nur wenn fn(a) und fn(b) unterschiedliche Vorzeichen hat
#ermittelt Nullstelle
