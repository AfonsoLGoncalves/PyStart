from abc import ABC, abstractmethod

class AbstractClass(ABC):

    def __init__(self):
        self.atributo = "Olá Mundo"

    def metodo (self, elemento: str) -> None:
        print(elemento)

    @abstractmethod
    def metodo_abstrato(self) -> None:
        pass

# Quando fazemos uma classe inteiramente de metodos abstratos apegamos a ídeia que se trata de uma interface.