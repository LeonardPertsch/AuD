"""
Fibonacci mit Memoisierung
==========================

Berechnet die n-te Fibonacci-Zahl rekursiv; bereits berechnete Werte
werden in einem Dictionary (storage) zwischengespeichert.

Laufzeit: O(n) statt O(2^n) ohne Memoisierung
"""

def fib(num, storage):
    if num <= 1:
        return num
    if num in storage:
        return storage[num]
    storage[num] = fib(num-1, storage) + fib(num-2, storage)

    return storage[num]
dic = {}
print(type(dic))
print(fib(10, dic))
