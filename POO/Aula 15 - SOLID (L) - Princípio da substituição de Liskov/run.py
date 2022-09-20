# Quebra do principior de LISKOV.
# Devemos visualizar a herança como uma extensão.

class PessoaA:

    def se_apresentar(self):
        print("Olá meu nome é PessoaA")

class PessoaB(PessoaA):

    def __init__(self):
        super().__init__()

    def se_apresentar(self):
        print("Estou alterando este metodo")


pessoa = PessoaA()
pessoa.se_apresentar()

pessoa2 = PessoaB()
pessoa2.se_apresentar()


def apresentar():
    print("Estou alterando nesse metodo")

pessoa.se_apresentar = apresentar
pessoa.se_apresentar()