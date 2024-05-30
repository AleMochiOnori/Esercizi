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
                print("libro prestato")
                return libro.disponibilità        
                       


    def restituisci_libro(self,titolo : Libro):
        for libro in self.catalogo :
            if titolo == libro.titolo and libro not in self.catalogo :
                self.aggiungi_libro()
                print("il libro è stato restituito")


    def mostra_libri_disponibili(self):
        for libro in self.catalogo:
            if libro.disponibilità == True:
                print("I libri sono :" , libro.titolo)


libro1 = Libro("Harry Potter", "Rowling")
LavoratoreBiblioteca = Biblioteca()
LavoratoreBiblioteca.aggiungi_libro(libro1)
LavoratoreBiblioteca.presta_libro("Harry potter")
LavoratoreBiblioteca.restituisci_libro(libro1)
LavoratoreBiblioteca.mostra_libri_disponibili()