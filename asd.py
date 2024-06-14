from abc import ABC , abstractmethod


class AbcAnimal(ABC):


    @abstractmethod
    def verso(self):
        pass


class Gatto(AbcAnimal):
    def __init__(self,nome) -> None:
        super().__init__()

        self.nome = nome

    def verso(self):
        return print("Bau")

    def describe(self,nome):
        print(f"{nome} fa il verso ") 

gatto = Gatto(nome="cikolino")     

gatto.describe("cikolo")


class Cane(AbcAnimal):
    def __init__(self) -> None:
        super().__init__()

    def verso(self):
        return print("ciao")

cane = Cane()

gatto.verso()        


