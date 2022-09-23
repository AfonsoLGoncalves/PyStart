from models import Insersor, Repositorio

class RepositorioFaker(Repositorio):
    def __init__(self):
        super().__init__()

    def select(self, name: int) -> None:
        return None

repo = RepositorioFaker()
insersor = Insersor(repo)

data = insersor.inserir_dados("Afonso", 25)
print(data)