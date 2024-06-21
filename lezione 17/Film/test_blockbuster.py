from film import Film
import unittest
from movie_genre import Drama,Azione,Commedia
from noleggio import Noleggio



class Test(unittest.TestCase):
    def setUp(self):
        self.avengers = Azione(id = 20 , title = "Avengers" , genere = "Azione",  penalità = 3)
        self.vanHellsing = Azione(id = 30,title = "Van Hellsing" , genere= "Azione" , penalità= 3)
        self.rambo = Azione(id=10 , title = "Rambo" , genere= "Azione" , penalità= 3)
        self.fastAndFurious = Azione(id= 22 , title = "Fast And Furious", genere="Azione " , penalità= 3)
        self.johnWick = Azione(id = 34, title = "John Wick",genere = "Azione" , penalità = 3)


