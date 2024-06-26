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
        asterischi = self.lato
        for lato in range(1,asterischi):    
            print("*", end=" ")
            if lato == asterischi:   
                print("****")
        for lato in range(1,asterischi): 
            print("*")
        for lato in range(1,asterischi + 1):    
            print("*", end=" ") 
       


caio = Quadrato(10)


caio.render()