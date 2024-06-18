class Veicolo:
    def __init__(self, marca : str , modello : str , anno : str):
        self.marca = marca 
        self.modello = modello
        self.anno = anno
        
        
        
    def descrivi_veicolo(self):
        print(f"Marca : {self.marca} , Modello : {self.modello} , Anno :  {self.anno}")
        
    
class Auto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: str , numero_porte : int):
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte
    