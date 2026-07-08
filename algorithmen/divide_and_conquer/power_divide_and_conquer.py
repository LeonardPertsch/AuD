"""
Potenzieren mit Divide and Conquer
==================================

Berechnet base^exponent, indem der Exponent rekursiv halbiert wird.

Laufzeit: O(log n) Rekursionstiefe
"""

def power(base, exponent):
    if(exponent == 0):
        return 1
    else:
        if(exponent == 1):
            return base
        else:
            half = exponent // 2
            half = half
            return power(base, half) * power(base, exponent-half)


print(power(2, 3))
#working
