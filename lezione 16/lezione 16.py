# Implementare una classe Media che rappresenti un media generico (ad esempio, un film o un libro) e una classe derivata Film che rappresenti specificamente un film. Gli studenti dovranno anche creare oggetti di queste classi, aggiungere valutazioni e visualizzare le recensioni.

# Specifiche della Classe Media:
 
# Attributi:
# - title (stringa): Il titolo del media.
# - reviews (lista di interi): Una lista di valutazioni del media, con voti compresi tra 1 e 5.

# Metodi:
# - set_title(self, title): Imposta il titolo del media.
# - get_title(self): Restituisce il titolo del media.
# - aggiungiValutazione(self, voto): Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).
# - getMedia(self): Calcola e restituisce la media delle valutazioni.
# - getRate(self): Restituisce una stringa che descrive il giudizio medio del media basato sulla media delle valutazioni.
# - ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
# - recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo, il voto medio, il giudizio e le percentuali di ciascun voto. Esempio di riassunto:
 
# Titolo del Film: The Shawshank Redemption
# Voto Medio: 3.80
# Giudizio: Bello
# Terribile: 10.00%
# Brutto: 10.00%
# Normale: 10.00%
# Bello: 30.00%
# Grandioso: 40.00%

# Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film, aggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione().



class Media:
    def __init__(self,title):
        self.title = title 
        self.reviews = []


    def set_title(self,title):
        self.title = title 

    def  get_titolo(self):
        return self.title   


    def aggiungiValutazione(self,voto):
        if voto >= 0 and voto <= 5 :
            self.reviews.append(voto)
            
    def getMedia(self):
        return sum(self.reviews) / len(self.reviews)
    
    def getRate(self):
        media  = self.getMedia()

        if media == 0 :
            return "Film is trash"
        elif media >= 1 and media <= 2:
            return "Terribile"
        elif media > 2 and media <= 3 :
            return "Normale"
        elif media > 3 and media <= 4 :
            return "Bello"
        elif media > 4 and media <= 5 :
            return  "Grandioso" 
        else :
            return "inserire un valore da uno a cinque"

    def ratePercentage(self,voto):
        numeroVolte = self.reviews.count(voto)
        numeroVolte = numeroVolte  * 100 / len(self.reviews)
        rounded = round(numeroVolte)
        return rounded


    def recensione(self):
        print(f"Titolo Film :  {self.get_titolo()}")
        print("Il voto medio è", self.getMedia())
        print("Giudizio",self.getRate())
        print(f"Terribile {self.ratePercentage(1)}, Normale {self.ratePercentage(2)}% , Bello {self.ratePercentage(3)}% grandioso {self.ratePercentage(4)}%")


class Film(Media):
    def __init__(self, title):
        super().__init__(title)





ilCocckettoDelizioso = Film("Star Wars")
ilCocckettoDelizioso.aggiungiValutazione(3)
ilCocckettoDelizioso.aggiungiValutazione(2)
ilCocckettoDelizioso.aggiungiValutazione(1)
ilCocckettoDelizioso.aggiungiValutazione(5)
ilCocckettoDelizioso.aggiungiValutazione(2)
ilCocckettoDelizioso.aggiungiValutazione(1)
ilCocckettoDelizioso.ratePercentage(2)
ilCocckettoDelizioso.recensione()



yee = Film("flavionchoi")
yee.aggiungiValutazione(2)