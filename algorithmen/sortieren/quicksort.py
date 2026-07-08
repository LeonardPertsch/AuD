"""
Quicksort
=========

Wählt ein Pivot-Element und zerlegt die Liste in kleinere, gleiche und
größere Elemente; die Teillisten werden rekursiv sortiert.

Laufzeit: O(n log n) im Mittel, O(n²) im schlechtesten Fall
"""

def quicksort(arr):
    if len(arr) <= 1:  # Basisfall: Eine Liste mit 0 oder 1 Element ist bereits sortiert
        return arr

    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]

    left = [x for x in arr if x < pivot]  # Alle Elemente kleiner als Pivot
    middle = [x for x in arr if x == pivot]  # Alle Pivots (bei doppelten Werten)
    right = [x for x in arr if x > pivot]  # Alle Elemente größer als Pivot
    # Rekursiver Aufruf für linke und rechte Seite
    return quicksort(left) + middle + quicksort(right)

# Test
Sortable_array = [5, 3, 2, 4, 9, 7, 0]
sorted_array = quicksort(Sortable_array)
print(sorted_array)  # Erwartet: [0, 2, 3, 4, 5, 7, 9]
