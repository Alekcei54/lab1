import math


def task24_int():
    """
    З початку доби минуло N секунд (N - ціле). Знайти кількість повних
    хвилин, що минули з початку останньої години.
    """
    # Введіть кількість секунд
    # Перевіряємо коректність вводу даних
    try:
      N = int(input("Введіть кількість секунд: "))
    except ValueError:
      print("Число повинно бути цілим!")
    else:
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
        denum=math.pow(4+((x**3)/5), 1/3)+math.log(math.fabs(x),2)
        # Нема необхідності окремо перевіряти ділення на 0, оскільки ви 
        # відстежуєте помилку ZeroDivisionError
    except ValueError:
        print("Помилка: Введіть коректне числове значення для x.")
    except ZeroDivisionError:
        print("Помилка: Ділення на нуль неможливе.")
    else:
        y = num / denum
        print(f"Значення y при x={x}: {y}")


def task1_bool():
    """
    Перевірити істинність висловлювання: «Число A є
позитивним».
    """
    try:
        a = int(input("Введіть число A: "))
    except ValueError:
        print("Помилка:Введіть ціле число для a, b та c.")
    else:
        is_positive = a>0

        print(is_positive)


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