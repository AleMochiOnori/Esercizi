class Documento:
    def __init__(self,testo : str):
        self.testo = testo

    def setText(self,testo):
        self.testo = testo

    def getText(self):
        return self.testo
    

    def isIntext(self,text):
        if text in self.getText():
            return True
        else :
            print("The text entered is not in the document")



class Email(Documento):
    def __init__(self, testo: str , mittente : str , destinatario : str , titoloDelMessaggio : str):
        super().__init__(testo)
        self.mittente = mittente
        self.destinatario = destinatario
        self.titoloDelMessaggio = titoloDelMessaggio


    def setMittente(self,mittente:str):
        self.mittente = mittente

    def getMittente(self):
        return self.mittente
    

    def setDestinatario(self,destinatario:str):
        self.destinatario = destinatario

    def getDestinatario(self):
        return self.destinatario
    
    def setTitoloDelMessagio(self,titoloDelMessaggio):
        self.titoloDelMessaggiov = titoloDelMessaggio

    def getTitoloDelMessaggio(self):
        return self.titoloDelMessaggio
    
    def setText(self, testo):
        self.testo = testo

    def getText(self):
        return f"From: {self.mittente} A : {self.destinatario}/n {self.titoloDelMessaggio}/n Messaggio : {self.titoloDelMessaggio}"

    def writeToFile(self, path):
        with open(path, "w" ) as document :
           lines =  self.getText()
           document.writelines(lines)  

    

class File(Documento):
    def __init__(self, testo: str,nomePercorso):
        super().__init__(testo)
        self.nomePercorso = nomePercorso
    

    def leggiTestoDaFile(self, path):
        with open(path, "r") as reader:
            linee = reader.readlines()
        return linee
    
    






    
    


    

