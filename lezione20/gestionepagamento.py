class Pagamento:
    def __init__(self):
        self.__pagamento = 0.0



    def set_pagamento(self,pagamento):
        self.__pagamento = pagamento 

    def get_pagamento(self):
        return self.__pagamento
    


    def dettagli_pagamento(self):
        if self.get_pagamento() > 10:
            return f"L'importo del pagamento è : {self.get_pagamento()}"
        



class PagamentoContanti(Pagamento):

    def __init__(self, importo):
        super().__init__()
        self.set_pagamento(importo)
    
    def dettagli_pagamento(self):
        if self.get_pagamento() > 10:
            return f"L'importo del pagamento è : {self.get_pagamento()} in contanti"

    def inPezziDa(self):
        banconote = [500,200,100,50,20,10,5,2,1,0.5,0.2,0.1]
        importo = self.get_pagamento()
        for banconota in banconote:
            pezzi = importo // banconota
            importo = round(importo - pezzi * banconota, 2)
            if pezzi != 0 and banconota >=5:
                return f"{pezzi} di banconote da €{banconota}"
            if pezzi != 0 and banconota < 5:
                return f"{pezzi} di monete da €{banconota}"


class PagamentoCartaDiCredito(Pagamento):
    def __init__(self,importo : float , nomeTitolareCarta : str , dataDiScadenza: float , numeroCartaDiCredito : int ):
        super().__init__()
        self.set_pagamento(importo)
        self.nomeTitolareCarta = nomeTitolareCarta
        self.dataDiScadenza = dataDiScadenza
        self.numeroCartaDiCredito = numeroCartaDiCredito

    def dettagli_pagamento(self):
        return f"Il pagamento è {self.get_pagamento()} con carta bancomat"
    


pagamento = Pagamento()

contanti = PagamentoContanti(150)

contanti.dettagli_pagamento()
contanti.inPezziDa()
