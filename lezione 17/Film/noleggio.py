from film import Film
from movie_genre import Drama,Azione,Commedia




class Noleggio:
    def __init__(self,film_list):
        self.film_list = film_list
        self.rented_films = {}

    def isAvaible(self,film):
        if film in self.film_list:
            print(f"Il film scelto è disponibile : {self.get_title()}")
            return True
        else : 
            print(f"Il film scelto non è disponibile : {self.get_title()}")
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
            print(f"Cliente: {clientID}! La penale da pagare per il film {self.get_title()} e' di {self.get_Penale()} euro!")
        return self.calcoloPenaleRitardo(days)
    

    def print_movies(self):
        for film in self.film_list:
            print(f"{film.get_title()} - {film.get_title()}")


    def printRentMovies(self,clientID):
        if clientID in self.rented_films.keys():
            print(self.rented_films.values())


    

            
        


        
                    