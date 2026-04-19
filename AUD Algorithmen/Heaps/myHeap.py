def heapify(n, i, arr):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(n, smallest, arr)
    pass
def transformToHeap(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        heapify(n, i, arr)





minHeap = list([0, 1, 2, 5, 8, 4, 3, 10, 11, 15, 3, 7])
transformToHeap(minHeap)
print(minHeap)