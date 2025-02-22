# try:
#     number = int(input("Введите число: "))
#     print(10/number)
# except ZeroDivisionError:
#     print("На ноль делить нельзя")
# except ValueError:
#     print("Надо ввести только целое число!")
# else:
#     print("Ошибок нет!")
# finally:
#     print("Программа завершена.")


def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a/b

try:
    print(divide(int(input()),int(input())))
except ZeroDivisionError as e:
    print(f"Ошибка: {e}")