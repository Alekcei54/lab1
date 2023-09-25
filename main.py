import math
def task24_int():
    """
    Знайти кількість повних хвилин, що минули з початку останньої години
    """
    # Введіть кількість секунд
    N = int(input("Введіть кількість секунд: "))

    # Знайдемо кількість хвилин, що минуло з початку останньої години
    minutes = (N // 60) % 60

    print("Кількість повних хвилин з початку останньої години:", minutes)
def task26():
    """
    Функція для розрахунку прикладу.
    """
    try:
        x = float(input("Введіть x: "))
        num = 4*math.tan(x*x)*math.sin(x)+1/5*math.sqrt(math.fabs((math.sin(x)*math.sin(x))*math.tan(x)))
        denum=math.cbrt(4+((x**3)/5))+math.log(math.fabs(x),2)
        if denum == 0:
            print("Ділення на нуль неможливе.")
        else:
            y = num / denum
            print(f"Значення y при x={x}: {y}")
    except ValueError:
        print("Помилка: Введіть коректне числове значення для x.")
    except ZeroDivisionError:
        print("Помилка: Ділення на нуль неможливе.")


def task1_bool():
    """
    Перевірити істинність висловлювання: «Число A є
позитивним».
    """
    try:
        a = int(input("Введіть число A: "))

        is_positive = a>0

        print(is_positive)
    except ValueError:
        print("Помилка:Введіть ціле число для a, b та c.")


if __name__ == "__main__":
    while True:
        print("\nОберіть опцію:")
        print("1. Вивести число з переставленими числами")
        print("2. Обрахувати приклад")
        print("3. Перевірити істинність висловлювання")
        print("0. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            task24_int()
        elif choice == "2":
            task26()
        elif choice == "3":
            task1_bool()
        elif choice == "0":
            break
        else:
            print("Невірний вибір. Виберіть 1, 2, 3 або 0.")