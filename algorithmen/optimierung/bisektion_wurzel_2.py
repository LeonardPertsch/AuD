"""
Bisektion: Wurzel aus 2
=======================

Berechnet √2 als Nullstelle von f(x) = x² - 2 mit dem
Bisektionsverfahren.
"""

def f(x):
    return x**2-2

def bisection(a,b,accuracy):
    c = (a+b)/2
    while abs(a-b)>accuracy:
        if f(c)*f(a)<0:
            b = c
        else:
            if f(c)*f(b)<0:
                a=c
            else:
                return c
        c = (a+b)/2

    return c


print(bisection(-10,10,0.0000001))
