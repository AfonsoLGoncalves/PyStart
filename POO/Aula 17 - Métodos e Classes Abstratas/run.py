from abs_class import AbstractClass

class Filha(AbstractClass):

    def apresentar_metodo(self) -> None:
        print(self.atributo)

    def metodo_abstrato(self) -> None:
        print("Implementando metodo abstrato")

filha = Filha()
filha.apresentar_metodo()
filha.metodo("estou aqui")
filha.metodo_abstrato()

# Erro
# abstractClass = AbstractClass()
# abstractClass.metodo("Fazendo algo")