print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numeroSecreto = 42
totalDeTentativas = 3
rodada = 1



for rodada in range(1, totalDeTentativas + 1):
    print("Tentativa {} de {}".format(rodada, totalDeTentativas))
    palpite = int(input("Digite um número entre 1 a 50: "))
    print("Você digitou o número", palpite)

    if palpite (palpite > 50 or palpite < 1):
        print("Você deve digitar um número entre 1 a 50!")
        continue

    #  Condições
    acertou = numeroSecreto == palpite
    maior = palpite > numeroSecreto
    menor = palpite < numeroSecreto


    while (maior or menor):
        if (acertou):
            print("Você acertou!")
            break
        else:
            if (maior):
                print("Errou! Você digitou um palpite maior que o número secreto")
            elif (menor):
                print("Errou! Você digitou um palpite menor que o número secreto")

print("Fim do jogo")
