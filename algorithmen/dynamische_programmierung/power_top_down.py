"""
Potenzieren (Top-down, rekursives Halbieren)
============================================

Berechnet base^exponent rekursiv, indem der Exponent halbiert und das
Teilergebnis quadriert wird.

Laufzeit: O(log n)
"""

def power_with_topdown(base, exponent):
    if exponent == 1:
        return base

    if exponent == 0:
        return 1
    else:
        half = exponent // 2
        tmp = power_with_topdown(base, half)
        if(exponent == 2* half):
            return tmp * tmp
        else:
            return tmp * tmp * base






print(power_with_topdown(2,5))
