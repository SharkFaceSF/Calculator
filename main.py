from functions import Arithmetic
from hard_functions import Engineering


operator = str(input('Введите оператор: '))
if operator in '+-/**':
    num1 = float(input('Введите первое число: '))

    num2 = float(input('Введите второе число: '))

    result = Arithmetic(num1, num2)
else:
    num1 = float(input('Введите число: '))

    hardresult = Engineering(num1)


if operator == "+":
    result.additions(num1, num2)

elif operator == "-":
    result.subtraction(num1, num2)

elif operator == "/":
    result.division(num1, num2)

elif operator == "*":
    result.multiplication(num1, num2)

elif operator == "**":
    result.сonstruction(num1, num2)

elif operator == "!":
    hardresult.fact(num1)

elif operator == "√":
    hardresult.sqrt(num1)

elif operator == "log":
    hardresult.log(num1)

elif operator == "[]":
    (hardresult.modul(num1))

