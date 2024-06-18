
from Paziente import Paziente
from Dottore import Dottore


class Fattura():
    def __init__(self, patient , doctor ):
        
        self.patient = patient
        self.doctor = doctor
        self.pazienti = []
        if self.isAValidDoctor() :
            self.patients = self.pazienti.count()
            self.fattura = self.patients
            self.salary = 0
        else:
            self.patient = None
            self.doctor = None
            self.fattura = None
            self.salary = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")




    def getSalary(self):
        salary =  self.parcella * self.patients
        return salary
    
    def getFatture(self):
        self.fattura = self.patients
        return self.fattura
    
    def addPatient(self,newPatient):
        self.pazienti.append(newPatient)
        self.fattura = self.getFatture()
        self.salry = self.getSalary()
        print(f"Alla lista del dottor {self.getLastName()} è stato aggiunto il paziente {self.getIDCode()}")


    def removePatient(self,idCode):
        self.pazienti.remove(idCode)
        self.fattura = self.getFatture()
        self.salry = self.getSalary()
        print(f"Alla lista del dottor {self.getLastName()} è stato rimosso il paziente {self.getIDCode()}")








