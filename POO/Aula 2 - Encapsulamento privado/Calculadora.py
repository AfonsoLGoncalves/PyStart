class Calculadora():
    def calcular(self, op, num1, num2):
        if op == "+":
            return self.__adicionar(num1, num2)
        elif op == "-":
            return self.__subtrair(num1, num2)
        else:
            print("Operação não é válida!")

    def __subtrair(self, num1, num2):
        return num1 - num2

    def __adicionar(self, num1, num2):
        return num1 + num2

calculadora = Calculadora()
# Operação de Subtração
resultado = (calculadora.calcular("-", 3, 2))
print(resultado)

# Operação de Adição
resultado2 = (calculadora.calcular("+", 14, 10))
print(resultado2)