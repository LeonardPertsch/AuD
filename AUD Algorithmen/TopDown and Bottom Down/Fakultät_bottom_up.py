def Fakultät_bottom_up(n):
    fak = 1
    for i in range(n+1):
        if i != 0:
            fak = fak * i

    return fak

print(Fakultät_bottom_up(150))