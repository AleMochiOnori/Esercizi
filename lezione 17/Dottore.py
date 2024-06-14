from persona import Persona


class Dottore(Persona):
    def __init__(self, first_name, last_name,specializzazione : str , parcella : float):
        super().__init__(first_name, last_name)
        if type(specializzazione) == str and type(parcella) == float:
            self.specializzazione = specializzazione
            self.parcella = parcella
        else :
            self.parcella = None
            print("La parcelal inserita non è un Float")

    def setSpecialization(self,specialization):
        if type(specialization) == str :
            self.specializzazione = specialization
        else : 
            print("Il messagio deve essere una stringa")


    def setParcel(self,parcel):
        if type(parcel) == float:
            self.parcella = parcel
        else :
            print("Il valore inserito non è un numero")


    def getSpecialization(self):
        return self.specializzazione
    

    def getParcel(self):
        return self.parcella
    

    def isAValidDoctor(self):
        if self.età > 30:
            print(f"Dottore {self.first_name} {self.last_name} è  valido")

        else : 
            print(f"Dottore {self.first_name} {self.last_name} non è valido")


    def doctorGreet(self):
        print(self.greet() , "e la mia specializazione  è " , self.getSpecialization())

    

