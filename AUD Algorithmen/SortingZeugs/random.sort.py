import random
def random_sort(array,a):
    sorted = True
    a = a+1

    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            sorted = False
    if sorted:
        return array,a

    else:

        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                number = random.choice([0,1])

                if number ==1:
                    array.append(array.pop(i))
        return random_sort(array,a)



array = [5,1,2,6,7,10,123,-1,5,10,122,582,1249,4,1,5,7,9,100,23,467,12334,6543,12456,12]

print(random_sort(array, 0))