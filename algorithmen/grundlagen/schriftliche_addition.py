"""
Schriftliche Addition
=====================

Addiert zwei Zahlen ziffernweise mit Übertrag – wie auf dem Papier.
Die Ziffern werden in Listen zerlegt und von rechts nach links verarbeitet.

Laufzeit: O(n) bei n Stellen
"""

def addition(a, b):
    ListA = [[] for _ in range(get_stellen(max(a, b)))]  # Max. Stellenanzahl nehmen
    ListB = [[] for _ in range(get_stellen(max(a, b)))]


    digitsA = get_single(a)[::-1]
    digitsB = get_single(b)[::-1]

    for i in range(len(digitsA)):
        ListA[i].append(digitsA[i])

    for i in range(len(digitsB)):
        ListB[i].append(digitsB[i])




    result = []
    übertrag = 0

    for i in range(len(ListA)):
        sum_value = sum(ListA[i]) + sum(ListB[i]) + übertrag
        result.append([sum_value % 10])
        übertrag = sum_value // 10


    if übertrag > 0:
        result.append([übertrag])

    result.reverse()
    result_for_return=[]
    for i in range(len(result)):
        result_for_return.append(result[i][0])
    return "".join(map(str, result_for_return))


def get_stellen(x):
    return len(str(abs(x)))


def get_single(x):
    return [int(d) for d in str(abs(x))]



print(addition(18, 1162))
