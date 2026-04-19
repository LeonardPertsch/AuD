def fib(num, storage):
    if num <= 1:
        return num
    if num in storage:
        return storage[num]
    storage[num] = fib(num-1, storage) + fib(num-2, storage)

    return storage[num]
dic = {}
print(type(dic))
print(fib(10, dic))