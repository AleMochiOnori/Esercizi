class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
        self.disponibilità = True

class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def aggiungi_libro(self, libro: Libro):
        if libro not in self.catalogo:
            self.catalogo.append(libro)
            print("Libro aggiunto al catalogo")

    def presta_libro(self, titolo):
        for libro in self.catalogo:
            if titolo == libro.titolo:
                if libro.disponibilità:
                    libro.disponibilità = False
                    print("Libro prestato")
                    return True
                else:
                    print("Libro non disponibile")
                    return False
        print("Libro non trovato nel catalogo")
        return False

    def restituisci_libro(self, titolo):
        for libro in self.catalogo:
            if titolo == libro.titolo:
                if not libro.disponibilità:
                    libro.disponibilità = True
                    print("Il libro è stato restituito")
                    return True
                else:
                    print("Il libro era già disponibile")
                    return False
        print("Il libro non è stato trovato nel catalogo")
        return False

    def mostra_libri_disponibili(self):
        print("Libri disponibili nel catalogo:")
        for libro in self.catalogo:
            if libro.disponibilità:
                print(f"- {libro.titolo} di {libro.autore}")

# Example usage
libro1 = Libro("Harry Potter", "J.K. Rowling")
biblioteca = Biblioteca()
biblioteca.aggiungi_libro(libro1)

# Prestare il libro
biblioteca.presta_libro("Harry Potter")
# Tentare di prestare di nuovo lo stesso libro
biblioteca.presta_libro("Harry Potter")
# Restituire il libro
biblioteca.restituisci_libro("Harry Potter")
# Mostrare libri disponibili
biblioteca.mostra_libri_disponibili()
