class MinhaClasse:

    estatico = "lhama" # Variável de classe (Váriaveis estáticas)

    def __init__(self, estado):
        self.estado = estado

    def print_estatico(self):
        estatico = 3
        print(estatico)

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(False)

MinhaClasse.estatico = "Programador" # Mudança contexto da classe
obj1.estatico = "Lhama"              # Mudança contexto do objeto


print(obj1.estatico)            # Acesso contexto do objeto
print(obj2.estatico)            # Acesso contexto do objeto
print(MinhaClasse.estatico)     # Acesso contexto da classe


obj1.print_estatico()