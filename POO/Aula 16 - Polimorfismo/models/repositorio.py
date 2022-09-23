from typing import Dict


class Repositorio:

    def insert(self, nome: str, idade: int) -> Dict:
        return {"nome": nome, "idade": idade}

    def insert(self, nome: str, idade: int) -> Dict:
        print("Inserindo dados {}, {}".format(nome, idade))
        return {"nome": nome, "idade": idade}
