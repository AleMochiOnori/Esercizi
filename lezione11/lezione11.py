class Film:
    def __init__(self,titolo,durata):
        self.titolo = titolo
        self.durata = durata



class Sala:
    def __init__(self, id, film_in_programmazione, posti_totali, posti_prenotati):
        self.id = id
        self.film_in_programmazione = film_in_programmazione
        self.posti_totali = posti_totali
        self.posti_prenotati = posti_prenotati



    def prenota_posti(self,num_posti):
        if num_posti != 0 :
            num_posti = self.posti_totali - self.posti_prenotati
            self.posti_prenotati = num_posti
            print("Posto prenotato")
        else :
            print("I posti sono finiti")
    
    def posti_disponibili(self):
        num_posti = self.posti_totali - self.posti_prenotati
        print(num_posti) 
    


class Cinema():
    def __init__(self):
        self.sale = []


    def aggiungi_sala(self,sala):
        self.sale.append(sala)
        print(f"sala numero {sala} aggiunta ")

    def prenota_film(self,titolo_film,num_posti):
        num_posti = num_posti.posti_totali - self.posti_prenotati
        if titolo_film == self.titolo:
            self.posti_prenotati = num_posti
            print("film prenotato")


film = Film("Van Hellsing", 2)
GestoreSala = Sala(45 , "Van Hellsing", 100 , 30)
GestoreSala.prenota_posti(0)
GestoreSala.posti_disponibili()
cliente = Cinema()
cliente.prenota_film("Van Hellsing", 20)