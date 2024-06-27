from abc import ABC,abstractmethod



class Forma(ABC):
 
    def __init__(self,nome) -> None:
        super().__init__()
        self.nome = nome
    @abstractmethod


    @abstractmethod    
    def getArea(self):
        pass

    @abstractmethod    
    def render(self):
        pass

class Quadrato(Forma):
    def __init__(self, lato) -> None:
        super().__init__("Quadrato")
        self.lato = lato
    

    def getArea(self):
        self.area = self.lato * 4
        return self.area
    

    def render(self):
        lenght = self.lato
        print("*" * (lenght))
        for lato in range(1,lenght-1):    
            print("*" , " " * (lenght -4),"*")
        print("*" * (lenght))    
      


 


caio = Quadrato(4)


caio.render()