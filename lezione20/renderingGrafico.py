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
    def __init__(self, lato):
        super().__init__("Quadrato")
        self.lato = lato
    

    def getArea(self):
        self.area = self.lato * self.lato
        return self.area
    

    def render(self):
        lenght = self.lato
        print("*" * (lenght))
        for lato in range(1,lenght-1):    
            print("*" , " " * (lenght -4),"*")
        print("*" * (lenght))
        print(f"L'area di questo quadrato è {self.getArea()} e i suoi lati sono di {self.lato} astertischi")    
      


 




class Rettangolo(Forma):
    def __init__(self,altezza , base):
        super().__init__("Rettangolo")
        self.altezza = altezza
        self.base = base


    def getArea(self):
        area = self.base * self.altezza
        return area


    def render(self):
        altezzaLenght = self.altezza
        baseLenght = self.base
        print("*" * baseLenght)
        for _ in range(1,altezzaLenght-1):
            print("*" , " " * (baseLenght-4), "*")
        print("*" * baseLenght)
        print(f"L'area di questo quadrato è {self.getArea()}. La sua base è di {self.base} e la sua altezza è di {self.altezza}")  






class Triangolo(Forma):
    def __init__(self,base,lato1,lato2):
        super().__init__("Triangolo")


rettangolo = Rettangolo(10,4)
rettangolo.render()