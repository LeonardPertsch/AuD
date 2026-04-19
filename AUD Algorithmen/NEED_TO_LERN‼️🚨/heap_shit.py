heap_list = [1,7,2,35,72,9,2,21,5,14,23,50,12]
def max_heapify(heap, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and heap[left] > heap[largest]:
        largest = left
    if right < n and heap[right] > heap[largest]:
        largest = right
    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        max_heapify(heap, n, largest)

def transform_heap(heap):
    n = len(heap)
    for i in range(len(heap)-1, -1, -1):
        max_heapify(heap, n, i)

def remove(heap):
    heap.remove(heap[0])
    transform_heap(heap)


transform_heap(heap_list)
remove(heap_list)

print(heap_list)
