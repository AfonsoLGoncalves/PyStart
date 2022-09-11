# Exemplo usando o typing e boas práticas: https://docs.python.org/3/library/typing.html
class Pessoa: # Substantivo

    def __init__(self, name: str, idade: int) -> None:
        self.name = name    # Substantivo
        self.idade = idade  # Substantivo

    def dirigir(self, veiculo: str) -> None:  # Verbos
        print("Dirigindo um(a) {}".format(veiculo))

    def cantar(self) -> None:                 # Verbos
        print("Shot through the heart and I'm to blame")

    def apresentar_idade(self) -> int:        # Verbos
        return self.idade

