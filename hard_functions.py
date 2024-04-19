class Engineering():
    def __init__(self, num1):
        self.num1 = num1

    def fact(self, num1):
        import math
        print(math.factorial(num1))

    def sqrt(self, num1):
        import math
        print(math.sqrt(num1))

    def log(self, num1):
        import math
        print(math.log(num1))

    def modul(self, num1):
        if '-' in str(num1):
            return float(str(num1)[1::])
        print(num1)