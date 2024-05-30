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