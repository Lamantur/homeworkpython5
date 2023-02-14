def two(number, a=1, b=-0.5, k=0):
    k = k+1
    if number == 1:
        print(f"Количество элементов - {k}, их сумма - {a}")
        return 0
    a = a+b
    two(number-1, a, -b/2, k)


two(int(input("Введите количество: ")))
