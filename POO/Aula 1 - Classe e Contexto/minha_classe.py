class ControleRemoto:
    def __init__(self, televisao: str, comodo: str):
        self.televisao = televisao
        self.comodo = comodo

    def avancar_canal(self):
        print("Canal avançado")

    def voltar_canal(self):
        print("Voltar o canal")

    def escolher_canal(self, canal: int):
        print("Alterando para o canal: {}".format(canal))

# Objeto
controle_sala = ControleRemoto("samsung", "sala") # Passando elementos padrões para os atributos

# Utilização de metodos e atributos
print(controle_sala.comodo)
print(controle_sala.televisao)
controle_sala.avancar_canal()
controle_sala.escolher_canal(44)

controle_quintal = ControleRemoto("LG", "quarto")
print(controle_quintal.comodo)
print(controle_quintal.televisao)