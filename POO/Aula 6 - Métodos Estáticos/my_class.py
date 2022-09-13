class MinhaClasse:

    def __init__(self, estado):
        self.estado = estado

    # Não tem acesso aos outros elementos da classe!
    @staticmethod
    def metodo_estatico():
        print("Estou no meu metodo estático :D")


obj = MinhaClasse(True)
MinhaClasse.metodo_estatico()

