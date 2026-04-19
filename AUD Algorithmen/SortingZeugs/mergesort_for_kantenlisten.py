def mergesort(edgelist):
    if len(edgelist) <= 1:  # Basisfall: Eine Liste mit 0 oder 1 Element ist bereits sortiert
        return edgelist

    Hlist = len(edgelist) // 2
    ListL = mergesort(edgelist[:Hlist])  # Rekursiver Aufruf für linke Hälfte
    ListR = mergesort(edgelist[Hlist:])  # Rekursiver Aufruf für rechte Hälfte

    ListS = []  # Ergebnisliste
    i, j = 0, 0

    while i < len(ListL) and j < len(ListR):
        if ListL[i] < ListR[j]:  # Vergleich der Elemente
            ListS.append(ListL[i])
            i += 1
        else:
            ListS.append(ListR[j])
            j += 1

    # Restliche Elemente aus ListL und ListR hinzufügen
    ListS.extend(ListL[i:])
    ListS.extend(ListR[j:])

    return ListS

edges = [
    (10, 2), (1, 3), (7, 4), (3, 5),
    (3, 6), (7, 6), (1, 7), (7, 8),
    (8, 9), (2, 10), (3, 7)
]

print(mergesort(edges))
