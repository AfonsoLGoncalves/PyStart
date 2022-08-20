import random

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numeroSecreto = round(random.randrange(1, 51))  # Randomiza número de 1 a 50
print(numeroSecreto)
totalDeTentativas = 0
rodada = 1
pontos = 500

print("Qual nível de dificuldade?")
print("(1) Fácil\n(2) Médio\n(3) Difícil")
nivel = int(input("Defina um nível: "))

if (nivel < 0 or nivel > 3):
    print("Digite um número válido")
else:
    match nivel:
        case 1:
            print("Modo fácil selecionado")
            totalDeTentativas = 20
        case 2:
            print("Modo médio selecionado")
            totalDeTentativas = 10
        case 3:
            print("Modo difícil selecionado")
            totalDeTentativas = 5

for rodada in range(1, totalDeTentativas + 1):
    palpite = int(input("Digite um número entre 1 a 50: "))
    print("Tentativa {} de {}".format(rodada, totalDeTentativas))  # String Interpolação
    print("Você digitou o número", palpite)

    if (palpite > 50 or palpite < 1):
        print("Você deve digitar um número entre 1 a 50!")
        continue

    #  Condições
    acertou = numeroSecreto == palpite
    maior = palpite > numeroSecreto
    menor = palpite < numeroSecreto

    # Possibilidade de resultados
    if (acertou):
        print("Você acertou!\nFez {} pontos!".format(pontos))
        break
    else:
        if (maior):
            print("Errou! Você digitou um palpite maior que o número secreto")
        elif (menor):
            print("Errou! Você digitou um palpite menor que o número secreto")
        pontosPerdidos = abs(numeroSecreto - palpite)
        pontos = pontos - pontosPerdidos

print("Fim do jogo")
