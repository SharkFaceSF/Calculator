num1 = int(input('Введите первое число: '))

num2 = int(input('Введите первое число: '))

operator = str(input('Введите оператор: '))


def additions(num1, num2):
    return print(num1 + num2)


if operator == "+":
    additions(num1, num2)