from typing import Type


class Casa:

    def __init__(self) -> None:
        self.__endereco = "Rua dos Limoeiros"

    def acender_luzes(self) -> None:
        print("Estou ascendendo as Luzes")

    def get_endereco(self) -> str:
        return self.__endereco

# Classe pessoa encontra-se dependente de outra classe
class Pessoa:

    def __init__(self, nome: str, local: Type[Casa]) -> None:
        self.__local = local
        self.__nome = nome

    def entrar_no_local(self) -> None:
        self.__local.acender_luzes()

    def apresentar_local (self) -> None:
        endereco = self.__local.get_endereco()
        print(endereco)

minha_casa = Casa()
ana = Pessoa("Ana", minha_casa)
ana.apresentar_local()