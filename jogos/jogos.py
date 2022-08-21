import forca
import adivinhacao

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

print("(1) Forca (2) Advinhação")

jogo = int(input("Qual Jogo?"))

if (jogo == 1):
    print("Jogando forca")
    forca.jogar()
elif (jogo == 2):
    print("jogando adivinhação")
    adivinhacao.jogar()