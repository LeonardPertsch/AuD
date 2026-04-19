a = [2, 3, 4, 5]
b = [0] * len(a)

b[0] = a[0]

for i in range(1, len(a)):
    b[i] = b[i - 1] + a[i]

print(b)
