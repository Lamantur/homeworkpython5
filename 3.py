
def chnech(numer, f=0):
    if numer == 0:
        print(f)
        return 0
    f = f*10+numer % 10
    return chnech(numer//10, f)


chnech(int(input("Введите число: ")))
