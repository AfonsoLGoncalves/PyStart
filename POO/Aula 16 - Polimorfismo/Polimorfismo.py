class PessoaA:

    def se_apresentar(self):
        print("Olá, sou a pessoa A")


class PessoaB(PessoaA):

    def __init__(self):
        super().__init__()

    # Isso aqui se trata de polimorfismo
    def se_apresentar(self):
        print("Estou alterando esse método")


class PessoaC(PessoaB):

    def __init__(self):
        super().__init__()

    def se_apresentar(self):
        print("testando polimorfismo")

pessoa = PessoaA()
pessoa.se_apresentar()

pessoa = PessoaB()
pessoa.se_apresentar()

pessoaC = PessoaC()
pessoaC.se_apresentar()