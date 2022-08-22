def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    print(letras_acertadas)

    # Condicionais
    enforcou = False
    acertou = False

    # Enquanto não enforcou e não acertou
    while (not enforcou and not acertou):
        palpite = input("Qual letra?")
        palpite = palpite.strip()

        index = 0
        for letra in palavra_secreta:
            if (palpite.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()
