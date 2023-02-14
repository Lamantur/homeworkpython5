import random


def ugadai(zagadka, popitka, i=10):
    if zagadka == popitka and i > 0:
        print("Вы угадали!")
        if input("Начать заного? (y/n): ") == "y":
            return ugadai(random.randint(0, 100), int(input("Угадайте задуманное число: ")))
        else:
            return 0
        return 0
    elif zagadka > popitka and i > 0:
        return ugadai(zagadka, int(input(f"Загаданное число больше, у вас осталось {i} попыток, попробуйте еще: ")), i-1)
    elif zagadka < popitka and i > 0:
        return ugadai(zagadka, int(input(f"Загаданное число меньше, у вас осталось {i} попыток, попробуйте еще: ")), i-1)
    elif i <= 0:
        print(
            f"Попытки закончились, вы не угадали, задуманное число: {zagadka}")
        if input("Начать заного? (y/n): ") == "y":
            return ugadai(random.randint(0, 100), int(input("Угадайте задуманное число: ")))
        else:
            return 0


print("Загадано число от 0 до 100, попробуйте угадать его за 10 попыток,")
ugadai(random.randint(0, 100), int(input("Угадайте задуманное число: ")))
