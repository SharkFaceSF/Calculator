num1 = int(input('Введите первое число: '))

num2 = int(input('Введите первое число: '))

operator = str(input('Введите оператор: '))


def additions(num1, num2):
    return print(num1 + num2)

def subtraction(num1, num2):
    return print(num1 - num2)

def division(num1, num2):
    return print(num1 / num2)


if operator == "+":
    additions(num1, num2)

elif operator == "-":
    subtraction(num1, num2)

elif operator == "/":
    division(num1, num2)