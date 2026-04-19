def fibonacci(n, storage):
    print(storage)
    if n == 1 or n == 0:
        return n
    if n in storage:
        return storage[n]
    storage[n] = fibonacci(n - 1, storage) + fibonacci(n - 2,storage)
    return storage[n]
storeage={}
print(fibonacci(10,storeage))