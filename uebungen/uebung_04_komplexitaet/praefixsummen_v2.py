"""
Übung 4: Präfixsummen (Variante 2, quadratisch)
===============================================

Berechnet dieselben Präfixsummen mit zwei verschachtelten Schleifen –
als Vergleich für die Komplexitätsanalyse.

Laufzeit: O(n²)
"""

a = [2, 3, 4, 5]
n = len(a)
b = [0] * n

for j in range(1, n + 1):
    for i in range(1, j + 1):
        b[j - 1] += a[i - 1]

print(b)
