from typing import Type

class Interruptor:
    def __init__(self, comodo: str):
        self.__comodo = comodo

    def acender(self) -> None:
        print(f"Acendendo {self.__comodo}")

    def apagar(self) -> None:
        print(f"Acendendo {self.__comodo}")
        print(f"Acendendo {self.__comodo}")


class Pessoa:

    def acender_luzes(self, interruptor: Type[Interruptor]):
        interruptor.acender()

    def desligando_luzes(self, interruptor: Type[Interruptor]):
        interruptor.apagar()

    def dormir(self) -> None:
        print("Foi dormir.")

afonso = Pessoa()
interruptor_quarto = Interruptor("quarto")
interruptor_cozinha = Interruptor("cozinha")

interruptor_quarto.acender()                # Chamada direta do método ascender
afonso.desligando_luzes(interruptor_quarto) # Chamada via associação de classe
afonso.acender_luzes(interruptor_cozinha)
afonso.dormir()

