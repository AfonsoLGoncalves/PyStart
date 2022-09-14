# Classe aberta para extensões, fechadas para modificações
'''
Pense na análogia de extensões de um navegador
    - O código binário de navegador encontra-se fechado para modificações
    - As extensões permitem extender a usabilidade do navegador
'''


class Circo:

    def apresenta(self, apresentador: any):
        apresentador.apresentar_show()


class Malabarista:

    def apresentar_show(self):
        print("Malabarista apresentando seu show!")


class Palhaco:

    def apresentar_show(self):
        print("Palhaço apresentando seu show!")


class Magico:

    def apresentar_show(self):
        print("Magico apresentado seu show!")


# Diferentes entradas geram diferentes resultados
magico = Magico()
magico.apresentar_show()