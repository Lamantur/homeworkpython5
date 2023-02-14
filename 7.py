def gsum(n, sum=0):
    if n == 0:
        return sum
    sum = sum + n

    return gsum(n-1, sum)


a = int(
    input("Для проверки равенства [1+2+...+n = n(n+1)/2] введите число n: "))
b: int = a*(a+1)/2

if gsum(a) == b:
    print(f"равенство для числа {a} верно")
else:
    print(f"равенство для числа {a} неверно")
