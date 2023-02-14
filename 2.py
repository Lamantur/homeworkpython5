
def chnech(numer, c=0, n=0):
    if numer == 0:
        print(f"четных чисел: {c}, нечетных чисел: {n}")
        return 0
    if (numer % 10) % 2 == 0:
        c = c+1
    else:
        n = n+1
    return chnech(numer//10, c, n)


chnech(int(input("Введите число: ")))
