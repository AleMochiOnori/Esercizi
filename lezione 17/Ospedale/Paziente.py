from persona import Persona


class Paziente(Persona):
    def __init__(self, first_name, last_name, id : str):
        super().__init__(first_name, last_name)
        self.__id = id

    def setIdCode(self,idCode):
        self.__id = idCode

    def getIdCode(self):
        return self.__id
    
    def patientInfo(self):
        print(f"Paziente : {self.getName()} {self.getLastName()}/n ID : {self.getIdCode()}")

    