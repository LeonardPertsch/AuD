"""
Brute Force: Maximum einer Liste
================================

Findet das größte Element, indem jedes Element einmal betrachtet wird.

Laufzeit: O(n)
"""

List = [1,5,2,4,7,8,11,59,123,539,12,682,124]

def brute(list):
    maximum = 0
    for i in list:
        if maximum < i:
            maximum = i
    return maximum
print(brute(List))
