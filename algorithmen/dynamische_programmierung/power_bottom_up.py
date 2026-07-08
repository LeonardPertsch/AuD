"""
Potenzieren (Bottom-up, binäre Exponentiation)
==============================================

Berechnet base^exponent iterativ: Zweierpotenzen des Exponenten werden
vorab berechnet und anschließend passend kombiniert.

Laufzeit: O(log n)
"""

def power(base,exponent):
    exp = [0,1]
    num = [1,base]
    i = 1
    while exp[i] <= exponent/2:
        exp.append(2*exp[i])
        num.append(num[i]*num[i])
        i = i+1
    result = 1
    exponentTest = 0
    i -= 1
    while exponentTest < exponent:
        tmp = exponentTest + exp[i]
        if tmp <= exponent:
            result = result * num[i]
            exponentTest = tmp
        i = i-1

    return result
print(power(2,3))
