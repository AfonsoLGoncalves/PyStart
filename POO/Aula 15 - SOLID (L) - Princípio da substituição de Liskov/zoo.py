from typing import Type

# Elemento mais generico acima, e os descendentes são espicificados a medida em que descemos a arvore.
class Animal:
    def comer(self) -> None:
        print("O animal está comendo!")

    def andar(self) -> None:
        print("O animal está andando!")

    def dormir(self) -> None:
        print("O animal está dormindo!")


class Lobos(Animal):
    def __init__(self):
        super().__init__()

    def uivar(self) -> None:
        print("AUuuuuuUUUUuuuuUUUUuuuuUUUUuuuUUUUUUuu!")


class Aves(Animal):
    def __init__(self):
        super().__init__()

    def cantar(self):
        print("Se eu demoro\nMas aqui eu vou morrer\nIsso é bom, mas eu não\nvivo sem você...")


class Falcao(Aves):
    def __init__(self):
        super().__init__()

    def falcao(self):
        print("Voar, Voar! Subir Subir!")


class Pinguim(Aves):
    def __init__(self):
        super().__init__()

    def escorregar(self) -> None:
        print("Ave encontra-se escorregando no gelo!")


class Pessoa:

    def observar(self, animal: Type[Aves]):
        print("Observando o passáro")
        animal.cantar()

roberto = Pessoa()
pinguim = Pinguim()
roberto.observar(pinguim)
