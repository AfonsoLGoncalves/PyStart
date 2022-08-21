def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    # Enquanto não enforcou e não acertou
    while (not enforcou and not acertou):
        palpite = input("Qual letra?")
        palpite = palpite.strip()

        index = 0
        for letra in palavra_secreta:
            if (palpite.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra, index))

            index = index + 1
        print("Jogando ...")


    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()