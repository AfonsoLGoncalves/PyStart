# https://wiki.python.org.br/EstruturaSequencial
# pythonbrasil - EstruturaSequencial

# 1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.
def aloMundo():
    return print("Alo Mundo!")


# 2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
def digiteNumero():
    num = input("Digite um número: ")
    return print(f"O número digitado foi {num}")


# 3. Faça um Programa que peça dois números e imprima a soma.
def soma(x, y):
    return print(x + y)


# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def notaMedia():
    QtdBimestres = 1
    somaNotaBimestrais = 0
    while QtdBimestres <= 4:
        somaNotaBimestrais += int(input(f"digite a {QtdBimestres}a nota: "))
        QtdBimestres += 1
    return print(somaNota/(QtdBimestres-1))


# 5. Faça um Programa que converta metros para centímetros.
def metrosParaCentimetros(metros):
        centimetros = metros * 1000
        return print (f"{metros} Metro(s) equivalem a {centimetros} centimetros")


# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
def calculoArea(raio):
    area = 3.14 * (raio ** 2)
    return print(area)


# 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.




"""
# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.
"""
def salarioMensal():
    salarioHora = int(input("Qual é o valor da sua hora salariada? "))
    horasMes = int(input("Quantas horas você trabalha por mês? "))
    return (salarioHora * horasMes)

"""
# 9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. 
Fórmula C = 5 * ((F-32) / 9).
"""
def fahrenheitParaCelsius():
    temperaturaFahrenheit = int(input("Qual é o valor da temperatura em Fahrenheit? "))
    calculoFahrenheitParaCelsius = (5 * ((temperaturaFahrenheit - 32) / 9))
    return print(f"A {temperaturaFahrenheit} Fahrenheit equivale a {calculoFahrenheitParaCelsius:,.4f} Celsius")


# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
def celsiusParaFahrenheit():
    temperaturaCelsius = int(input("Qual é o valor da temperatura em Celsius?"))
    calculoCelsiusParaFahrenheit = 1.8 * temperaturaCelsius + 32
    return print(f"A {temperaturaCelsius}  equivale a {calculoCelsiusParaFahrenheit:,.4f} Fahrenheit")


"""
11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    a. o produto do dobro do primeiro com metade do segundo .
    b. a soma do triplo do primeiro com o terceiro.
    c. o terceiro elevado ao cubo.
"""
def CalculadoraNumerosInteiros(x, y, z):
    resultadoCalculoA = (x * 2) + (y / 2)
    resultadoCalculoB = (x * 3) + z
    resultadoCalculoC = z ** 3
    return print (f"a. {resultadoCalculoA}\n"
            f"b. {resultadoCalculoB}\n"
            f"c. {resultadoCalculoC}\n")

"""
# 12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
usando a seguinte fórmula: (72.7*altura) - 58
"""
def CalculoPesoIdeal (h):
    pesoIdeal = (72.7 * h) - 58
    return print (pesoIdeal)


"""
13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
utilizando as seguintes fórmulas:
    a. Para homens: (72.7*h) - 58
    b. Para mulheres: (62.1*h) - 44.7
"""
def CalculoPesoIdeal (h, genero):
    if genero == "homem":
        pesoIdeal = (72.7 * h) - 58
    else:
        pesoIdeal = (62.1* h) - 44.7
    return print (pesoIdeal)


"""
14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite
e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
"""

"""
15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e 
mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    a. Para homens: (72.7*h) - 58
    b. Para mulheres: (62.1*h) - 44.7
    c. quanto pagou ao sindicato.
    d. o salário líquido.
    e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
        + Salário Bruto : R$
        - IR (11%) : R$
        - INSS (8%) : R$
        - Sindicato ( 5%) : R$
        = Salário Liquido : R$
"""

"""
16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser 
pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas 
de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

"""
17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 
18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
        * comprar apenas latas de 18 litros;
        * comprar apenas galões de 3,6 litros;
        * misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre 
        arredonde os valores para cima, isto é, considere latas cheias. 
"""

"""
# 18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de 
Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
