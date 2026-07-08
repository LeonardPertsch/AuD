"""
Greedy: Münzrückgabe
====================

Gibt Wechselgeld mit möglichst wenigen Münzen zurück, indem immer die
größte noch passende Münze gewählt wird.

Laufzeit: O(Anzahl Münzarten + Anzahl Münzen)
"""

coins = [200, 100, 50, 20, 10, 5, 2, 1]

def coinsback(coinpool, value_in, Kosten):
    used_coins=[]
    zurück = value_in-Kosten
    i = 0

    for coin in coinpool:
        while zurück >= coin:
            used_coins.append(coin)
            zurück -= coin
    return used_coins
print(coinsback(coins, 550, 100))
