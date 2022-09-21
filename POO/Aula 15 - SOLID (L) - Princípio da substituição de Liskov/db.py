from typing import Type


class Conexao:

    def conectar(self) -> None:
        print("Conectando o banco de dados")

    def desconectar(self) -> any:
        print("Desconectando o banco de dados")


class PostgreSQLRepo(Conexao):

    def __init__(self):
        super().__init__()

    def select(self) -> None:
        self.conectar()
        print('SELECT * FROM table')
        self.desconectar()

    def insert(self) -> None:
        self.conectar()
        print("INSERT INTO table")
        self.desconectar()


class CasoDeUso:

    def buscar(self, db_repo: Type[PostgreSQLRepo]) -> any:
        db_repo.select()

    def inserir(self, db_repo: Type[PostgreSQLRepo]) -> any:
        db_repo.insert()

caso = CasoDeUso()
db = PostgreSQLRepo()
caso.buscar(db)
caso.inserir(db)