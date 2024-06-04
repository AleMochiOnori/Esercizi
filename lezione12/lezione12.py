class Libro :
    def __init__(self, titolo , autore):
        self.titolo = titolo 
        self.autore = autore
        self.disponibilità = True



class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def aggiungi_libro(self,libro : Libro):
        if libro not in self.catalogo:
            libro.disponibilità = True
            self.catalogo.append(libro)
            print("Libro Aggiunto al catalogo")



    def presta_libro(self,titolo)  :
        for libro in self.catalogo :
            if titolo == libro.titolo:
                libro.disponibilità = False
                print("libro prestato ")
                return libro.disponibilità        


    def restituisci_libro(self,titolo : Libro):
        for libro in self.catalogo :
            if titolo == libro.titolo and libro.disponibilità == False:
                self.disponibilità = True
                print("il libro è stato restituito")

    def mostra_libri_disponibili(self):
        if self.disponibilità == True:
            for libro in self.catalogo:
                print("I libri sono :" , libro.titolo)


libro1 = Libro("Harry Potter", "Rowling")
LavoratoreBiblioteca = Biblioteca()
LavoratoreBiblioteca.aggiungi_libro(libro1)
LavoratoreBiblioteca.presta_libro("Harry Potter")
LavoratoreBiblioteca.restituisci_libro("Harry Potter")
LavoratoreBiblioteca.mostra_libri_disponibili()








class MovieCatalog:
    def __init__(self):
        self.catalogo = {}


    def add_movies(self,director_name, movies):
        if director_name:
            self.catalogo.update({director_name : movies})
            print("Film aggiunto al catalogo")
        else :
            print("New record")    

    
    def remove_movie(self, director_name, movie_name):
        if director_name in self.catalogo.keys() and movie_name in self.catalogo.values():
           self.catalogo.pop(movie_name)
           print("Film rimosso dal catalogo")
        else : 
            print("Il film non esiste")   
   

    def list_directors(self):
        for a,b in self.catalogo.items():
            print(f"I registi sono : {a}")
 

    def get_movies_by_director(self,director_name):
        for a,b in self.catalogo.items():
            if director_name == a :
                print(f"I Film Del regista sono {b}")
                return b
            

movies = MovieCatalog()
movies.add_movies("Flavio","pirati dei caribi")
movies.remove_movie("Flavio","pirati dei caribi")
movies.list_directors()
movies.get_movies_by_director("Flavio")
