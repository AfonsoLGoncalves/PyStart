class MinhaClasse:

    estatico = "lhama" # Variável de classe (Váriaveis estáticas)

    def __init__(self, estado):
        self.estado = estado

    def print_estatico(self):
        print(self.estatico)

    @classmethod
    def mudar_estatico(cls):
        cls.estatico = "Programador"    # == MinhaClasse.estatico = "Programador"



obj1 = MinhaClasse(True)
obj2 = MinhaClasse(False)

# Mudando o contexto de classe
obj1.mudar_estatico()

# Mudança repercurti para todos os objetos da Classe
obj1.print_estatico()
obj2.print_estatico()

print(MinhaClasse.estatico)