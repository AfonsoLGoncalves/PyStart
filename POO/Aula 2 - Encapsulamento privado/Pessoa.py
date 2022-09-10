class Pessoa:
    def __init__ (self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf  # Encapsulamento privado (Atributo)

    def correr(self): # Encapsulamento Público
        print("Estou correndo!")

    def beber(self, bebida):
        if bebida == "cerveja":
            self.__apresentar_documento()
        print(f'Estou bebendo {bebida}, GLUP GLUP!')

    def __apresentar_documento(self):  # Encapsulamento privado (Método)
        print(f'Aqui está o meu CPF:{self.__cpf}')

afonso = Pessoa("Afonso", 25, "000.000.000-00")
afonso.beber("cerveja")
afonso.beber("coca-cola")

