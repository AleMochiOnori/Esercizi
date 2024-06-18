from film import Film




class Noleggio(Film):
    def __init__(self, id, title,film_list):
      super().__init__(id, title)
      self.film_list = film_list
      self.rented_films = {}

    def isAvaible(self,film):
        if film in self.film_list:
            print(f"Il film scelto è disponibile : {self.title}")
            return True
        else : 
            print(f"Il film scelto non è disponibile : {self.title}")
            return False
    

    def rentAMovie(self,film,clientID):
        if self.isAvaible():
            self.film_list.remove(film)
            self.rented_films.update({clientID : []})
            for Id , films in self.rented_films.items():
                films.append(film)
            print(f"il Cliente {clientID} ha noleggiato il film {film}")
        else:
            print(f"Il film scelto : {film} non è disponibile")

    def giveBack(self,film,clientID,days):
        if film.id == clientID :
            for id , film in self.rented_films.items():
                film.remove(film)
            self.film_list.append(film)

        
                    