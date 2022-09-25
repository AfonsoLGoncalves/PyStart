from abc import ABC, abstractmethod

class AveVoadora(ABC):

    @abstractmethod
    def comer(self):
        raise "Should Implement comer method"

    @abstractmethod
    def voar(self):
        raise "Should Implement comer method"

    @abstractmethod
    def gritar(self):
        raise "Should Implement comer method"

# Interface mais especificas com intuito de classes que herdem utilizem todos os
# metodos abstratos.
class AveNaoVoadora(ABC):

    @abstractmethod
    def comer(self):
        raise "Should Implement comer method"

    @abstractmethod
    def gritar(self):
        raise "Should Implement comer method"