need_to_sort_list = [5,1,2,5,7,19,12,15,63,2,0,-5,-10]


def bubble_sort(arr):
        for i in range(len(arr)):
            print(arr)
            for j in range(len(arr)-1, i, -1):
                if arr[j] > arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]

        return arr

print(bubble_sort(need_to_sort_list))