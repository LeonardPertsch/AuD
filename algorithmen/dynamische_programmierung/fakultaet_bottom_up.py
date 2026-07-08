"""
Fakultät (Bottom-up)
====================

Berechnet n! iterativ von 1 bis n – klassisches Bottom-up-Schema.

Laufzeit: O(n)
"""

def Fakultät_bottom_up(n):
    fak = 1
    for i in range(n+1):
        if i != 0:
            fak = fak * i

    return fak

print(Fakultät_bottom_up(150))
