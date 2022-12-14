# https://wiki.python.org.br/EstruturaSequencial
# pythonbrasil - EstruturaSequencial

# 1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.
def alo_mundo():
    return print("Alo Mundo!")


# 2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
def digite_numero():
    num = input("Digite um número: ")
    return print(f"O número digitado foi {num}")


# 3. Faça um Programa que peça dois números e imprima a soma.
def soma():
    x = int(input("Digite um número para realizar soma: "))
    y = int(input("Digite outro número para realizar soma: "))
    return print(x + y)


# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def nota_media():
    qtd_bimestres = 1
    soma_nota_bimestrais = 0
    while qtd_bimestres <= 4:
        soma_nota_bimestrais += int(input(f"digite a {qtd_bimestres}a nota: "))
        qtd_bimestres += 1
    return print(soma_nota_bimestrais/(qtd_bimestres-1))


# 5. Faça um Programa que converta metros para centímetros.
def metros_para_centimetros(metros):
    centimetros = metros * 1000
    return print(f"{metros} Metro(s) equivalem a {centimetros} centimetros")


# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
def calculo_area():
    raio = int(input("Digite o raio de um círculo, para calcular a área: "))
    area = 3.14 * (raio ** 2)
    return print(f"A area do círculo é igual a: {area}.")


# 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
def dobro_area_quadrado():
    area_quadrado = int(input("Digite a area do quadrado: "))
    dobro_area_do_quadrado = area_quadrado ** 2
    return print(f"O dobro da area do quadrado é igual a: {dobro_area_do_quadrado}")


# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.
def salario_mensal():
    salario_hora = int(input("Qual é o valor da sua hora salariada? "))
    horas_mes = int(input("Quantas horas você trabalha por mês? "))
    return salario_hora * horas_mes


# 9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# Fórmula C = 5 * ((F-32) / 9).
def fahrenheit_para_celsius():
    temperatura_fahrenheit = int(input("Qual é o valor da temperatura em Fahrenheit? "))
    calculo_fahrenheit_para_celsius = (5 * ((temperatura_fahrenheit - 32) / 9))
    return print(f"A {temperatura_fahrenheit} Fahrenheit equivale a {calculo_fahrenheit_para_celsius:,.4f} Celsius")


# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
def celsius_para_fahrenheit():
    temperatura_celsius = int(input("Qual é o valor da temperatura em Celsius?"))
    calculo_celsius_para_fahrenheit = 1.8 * temperatura_celsius + 32
    return print(f"A {temperatura_celsius}  equivale a {calculo_celsius_para_fahrenheit:,.4f} Fahrenheit")


# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#     a. o produto do dobro do primeiro com metade do segundo .
#     b. a soma do triplo do primeiro com o terceiro.
#     c. o terceiro elevado ao cubo.
def calculadora_numeros_inteiros():
    # Adição valores as variaveis presentes:
    pedido = 1
    x = 0
    y = 0
    z = 0

    while pedido <= 3:
        if pedido <= 2:
            x = int(input(f"Digite 1o número inteiro: "))
            y = int(input(f"Digite 2o número inteiro: "))
            pedido = pedido + 2
        else:
            z = float(input(f"Para o {pedido}o número, digite um número real: "))
            pedido = pedido + 1

    resultado_calculo_a = (x * 2) + (y / 2)
    resultado_calculo_b = (x * 3) + z
    resultado_calculo_c = z ** 3
    return print(
        "Resultados foram iguais a:\n"
        f"a. ({x} * 2) + ({y} / 2) = {resultado_calculo_a}\n"
        f"b. ({x} * 3) + {z}      = {resultado_calculo_b}\n"
        f"c. {z} ** 3            = {resultado_calculo_c}\n"
    )


# 12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58
def calculo_peso_ideal(h):
    peso_ideal = (72.7 * h) - 58
    return print(peso_ideal)


# 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
#     a. Para homens: (72.7*h) - 58
#     b. Para mulheres: (62.1*h) - 44.7
def calculo_peso_ideal_genero(h, genero):
    if genero == "homem":
        peso_ideal = (72.7 * h) - 58
    else:
        peso_ideal = (62.1 * h) - 44.7
    return print(peso_ideal)


# 14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu
# trabalho.Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São
# Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia
# a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite
# e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
def calculo_quilo_excedente(peso_de_peixe):
    peso_estabelecido_por_lei = 50
    if peso_de_peixe > peso_estabelecido_por_lei:
        excesso_qtde_quilos = peso_de_peixe - 50
        valor_multa = excesso_qtde_quilos * 4.00
        return print(
                f"Devido o valor estipulado por lei {peso_estabelecido_por_lei}\nFoi excedido o peso em "
                f"{excesso_qtde_quilos} ocasionando o pagamento de 4 reais por quilo excedente, totalizando: "
                f"{valor_multa}"
        )
    else:
        print("Não teve excedente do peso estipulado por lei, não necessitando pagamento de multas.")


# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e
# mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#     a. Para homens: (72.7*h) - 58
#     b. Para mulheres: (62.1*h) - 44.7
#     c. quanto pagou ao sindicato.
#     d. o salário líquido.
#     e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
#         + Salário Bruto : R$
#         - IR (11%) : R$
#         - INSS (8%) : R$
#         - Sindicato ( 5%) : R$
#         = Salário Liquido : R$
def calculo_salario_liquido():
    # Calculo salário mensal bruto
    valor_horas_trabalhadas = int(input("quanto você ganha por horas?"))
    horas_trabalhadas_mes = int(input("quanto você ganha por horas?"))
    salario_bruto_mensal = valor_horas_trabalhadas * horas_trabalhadas_mes

    # Descontos saláriais
    ir = salario_bruto_mensal * 0.11
    inss = salario_bruto_mensal * 0.08
    sindicato = salario_bruto_mensal * 0.05

    # Calculo salário líquido
    salario_liquido = salario_bruto_mensal - (ir + inss + sindicato)

    return print(f"+ Salário Bruto : R${salario_bruto_mensal}\n"
                 f"- IR (11%) : R${ir}\n"
                 f"- INSS (8%) : R${inss}\n"
                 f"- Sindicato ( 5%) : R${sindicato}\n"
                 f"= Salário Liquido : R${salario_liquido}\n")


# 16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas
# de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço
# total.
def programa_loja_de_tintas():
    tamanho_area_a_ser_pintada = int(input("Digite o tamanho da area a ser pintada?"))
    litros_de_tinta = tamanho_area_a_ser_pintada / 3
    qtd_latas_de_tintas = litros_de_tinta // 18
    valor_total_latas_de_tintas = qtd_latas_de_tintas * 80.0

    return print(f"qtde de latas: {qtd_latas_de_tintas}\n valor latas de tintas: {valor_total_latas_de_tintas}\n")


# 17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida
# em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#         * comprar apenas latas de 18 litros;
#         * comprar apenas galões de 3,6 litros;
#         * misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre
#         arredonde os valores para cima, isto é, considere latas cheias.
def programa_loja_de_tintas_2():
    pass


# 18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de
# Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
def calculadora_download():
    tamanho_arquivo = int(input("Qual é o tamanho do arquivo em MegaBytes? "))
    velocidade_internet = int(input("Informe a velocidade da sua internet? "))
    velocidade_download_em_segundos = int(tamanho_arquivo / (velocidade_internet/8))
    velocidade_download_em_minutos = 0

    # Transformando segundos em minutos
    while velocidade_download_em_segundos > 59:
        velocidade_download_em_minutos += 1
        velocidade_download_em_segundos -= 60

    # Impressão do resultado
    return print(f"O tempo do download em média será: {velocidade_download_em_minutos} minuto(s) e "
                 f"{velocidade_download_em_segundos} segundo(s)")
