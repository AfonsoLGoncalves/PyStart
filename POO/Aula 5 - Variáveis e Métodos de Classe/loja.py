class Loja:

    tarifa = 1.03

    def __init__(self, endereco: str) -> None:
        self.__endereco = endereco

    def apresentar_endereco(self) -> None:
        print(self.__endereco)

    # Contexto diretamente associado a classe
    # Decorador
    @classmethod
    def vender(cls) -> int:
        return 40 * cls.tarifa

    @classmethod
    def alterar_tarifa(cls, nova_tarifa: int) -> None:
        cls.tarifa = nova_tarifa


loja_praia = Loja("Santos")
loja_centro = Loja("São Paulo")

loja_praia.apresentar_endereco() #Santos

print(loja_praia.vender())       #Venda 1
print(loja_centro.vender())      #Venda 1

loja_centro.alterar_tarifa(1.50)

print(loja_praia.vender())       #Venda 2
print(loja_centro.vender())      #Venda 2

