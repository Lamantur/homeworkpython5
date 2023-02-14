def calc():
    x = input("Введите операцию (+, -, *, / или 0 для выхода): ")
    if x != "0":
        a = input("Введите первое число: ")
        if a.isdigit() and a < 2147483647 and a > -2147483648:
            a = int(a)
        else:
            print(
                "введено неверное значение, либо слишком большое число, попробуйте ввести заного")
            return calc()

        b = int(input("Введите второе число: "))
        if b.isdigit() and b < 2147483647 and b > -2147483648:
            b = int(b)
        else:
            print(
                "введено неверное значение, либо слишком большое число, попробуйте ввести заного")
            return calc()
    if x != "0" and x != "+" and x != "-" and x != "*" and x != "/":
        print("введено неверное значение, попробуйте ввести заного")
        return calc()
    if x == "0":
        return 0
    elif x == "+":
        print(a+b)
        return calc()
    elif x == "-":
        print(a-b)
        return calc()
    elif x == "*":
        print(a*b)
        return calc()
    elif x == "/":
        if b != 0:
            print(a/b)
        else:
            print("нельзя делить на ноль")
        return calc()
    else:
        print("введен неверный символ")


calc()
