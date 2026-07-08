"""
Eigenes Dictionary mit Hash-Funktion
====================================

Einfache Hash-Tabelle mit Verkettung (Listen pro Bucket): Wörter werden
über ihre Zeichencodes auf einen Index abgebildet.
"""

dic_size = 10
my_hash = [[] for place in range(dic_size)]

def hash_funktion(word, length):
    if not word:
        return 0
    return int(''.join(str(ord(char)) for char in word)) % length


def add(dic, key, value):
    hash_key = hash_funktion(key, len(dic))
    dic[hash_key] += [(key, value)]


def find(dic, key):
    hash_value = hash_funktion(key, len(dic))
    hashlist = dic[hash_value]
    if not hashlist:
        return None
    return hashlist[0][1]

add(my_hash, 'a', 1)
add(my_hash, 'b', 4)
add(my_hash, 'c', 2)
add(my_hash, 'd', 3)
add(my_hash, '0', 100)
print(find(my_hash, '5'))
