test_list = (1, 3, 5, 2, 0, 7, 99, 12, 4,100)


def mergesort(List):
    if len(List) <= 1:
        return List  # Basisfall: Liste mit 0 oder 1 Element ist bereits sortiert

    half_list = len(List) // 2
    listL = mergesort(List[:half_list])  # Linke Hälfte rekursiv sortieren
    listR = mergesort(List[half_list:])  # Rechte Hälfte rekursiv sortieren

    ergebnis = ()
    i, j = 0, 0  # Indizes für das Mergen

    # **Mergen der sortierten Teillisten**
    while i < len(listL) and j < len(listR):
        if listL[i] < listR[j]:
            ergebnis += (listL[i],)  # Kleineres Element anfügen
            i += 1
        else:
            ergebnis += (listR[j],)
            j += 1


    # **Restliche Elemente von listL anhängen, falls vorhanden**
    ergebnis += listL[i:]

    # **Restliche Elemente von listR anhängen, falls vorhanden**
    ergebnis += listR[j:]

    return ergebnis  # Fertiges sortiertes Tupel zurückgeben


# **Testlauf**
sorted_list = mergesort(test_list)
print(sorted_list)
