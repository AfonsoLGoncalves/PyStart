# A idéia de Getter e Setter é tratar atributos como se fossem estados

class Alarme:

    def __init__(self, estado: bool) -> None:
        self.__estado = estado

    def get_estado(self) -> bool:
        return self.__estado

    def set_estado(self, valor: bool) -> None:
        if isinstance(valor, bool):
            self.__estado = valor

al = Alarme(False)
al.set_estado("Isinstance não vai permitir a mudança!")
al.set_estado(True)
print(al.get_estado())



