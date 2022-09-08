import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    # Selecionando palavra randomicamente
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()


    letras_acertadas = ["_" for letra in palavra_secreta] # List Comprehensions
    print(letras_acertadas)

    # Condicionais
    enforcou = False
    acertou = False
    erros = 0

    # Enquanto não enforcou e não acertou
    while (not enforcou and not acertou):
        palpite = input("Qual letra? ")
        palpite = palpite.strip().upper()

        if palpite in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if palpite == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print(f"Ops, você errou! Faltam {6 - erros} tentativas.")

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        return print("Parabéns você acertou a palavra secreta")
    else:
        return print("Você perdeu! Não desanime continue tentando!")
    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()
