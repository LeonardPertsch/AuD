def heapify(arr, n, i):
    largest = i  # Set root as largest
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify affected subtree


def transformToHeap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):  # Build heap (n//2-1) da das der Index des letzten Elternknotens, ab (n//2) sind alles Blätter
        heapify(arr, n, i)


# Beispiel
minHeap = list([0, 1, 2, 5, 8, 4, 3, 10, 11, 15, 3, 7])
transformToHeap(minHeap)
print(minHeap)
