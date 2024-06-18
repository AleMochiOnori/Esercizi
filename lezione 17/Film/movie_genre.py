from film import Film


class Drama(Film):
    def __init__(self, id, title , genere = "Drama" , penalità = 2):
        super().__init__(id, title)
        self.genere = genere
        self.__penalità = penalità

    def get_genere(self):
        return self.genere
    

    def get_Penale(self):
        return self.__penalità
    


    def calcolaPenaleRitardo(self):
        self.__penalità = self.__penalità + self.__penalità
        return self.__penalità
    

class Azione(Film):
    def __init__(self, id, title , genere = "Azione" , penalità = 3):
        super().__init__(id, title)
        self.genere = genere
        self.__penalità = penalità

    def get_genere(self):
        return self.genere
    

    def get_Penale(self):
        return self.__penalità
    


    def calcolaPenaleRitardo(self):
        self.__penalità = self.__penalità + self.__penalità
        return self.__penalità


class Commedia(Film):
    def __init__(self, id, title, genere = "Commedia" , penalità = 2.50):
        super().__init__(id, title)
        self.genere = genere
        self.__penalità = penalità

    def get_genere(self):
        return self.genere
    

    def get_Penale(self):
        return self.__penalità
    

    def calcolaPenaleRitardo(self):
        self.__penalità = self.__penalità + self.__penalità
        return self.__penalità

