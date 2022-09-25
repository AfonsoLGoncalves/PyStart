from interface import AveVoadora, AveNaoVoadora

class Canario(AveVoadora):

    def comer(self):
        print("Estou comendo!")

    def voar(self):
        print("Estou voando!")

    def gritar(self):
        print("Estou gritando!")


class Pinguim(AveNaoVoadora):

    def comer(self):
        print("Estou comendo!")
        self.__acasalar()

    def gritar(self):
        print("Estou comendo!")

    def __acasalar(self):
        print("Agora irei acasalar...")