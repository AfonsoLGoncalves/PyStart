class Repositorio:

    def select(self, db_connection: any) -> None:
        conection = db_connection.conectar()
        print(f"Conectei ao banco de dados {conection}")
        print("fazendo um SELECT * FROM...")
        db_connection.desconectar()

    def insert(self, db_connection: any) -> None:
        conection = db_connection.conectar()
        print(f"Conectei ao banco de dados {conection}")
        print("fazendo um SELECT Values...")
        db_connection.desconectar()

