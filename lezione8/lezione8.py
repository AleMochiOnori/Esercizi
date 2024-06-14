from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
       pass

class Circle(Shape):
    def __init__(self,raggio):
        super().__init__()
        self.raggio = raggio
        self.area_CERCHIO = 3,14 * (raggio**2)

    def area(self):
        return self.area_CERCHIO
    
class Rectangle(Shape):
    def __init__(self,lato1,lato2,lato3,lato4):
        super().__init__()
        self.perimetro_rettangolo = lato1,lato2,lato3,lato4   

    def area_rettangolo(self):
        return self.perimetro_rettangolo  
    
##################################################################################################


