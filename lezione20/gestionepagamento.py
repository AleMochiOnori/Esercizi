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
        result = []
        for banconota in banconote:
            pezzi = importo // banconota
            importo = round(importo - pezzi * banconota, 2)
            if pezzi != 0 and banconota >=5:
                if pezzi == 1 :
                    result.append(f"{pezzi} pezzo di banconota da {banconota}")
                else :
                    result.append(f"{pezzi} pezzi di banconote da €{banconota}")
            if pezzi != 0 and banconota < 5:
                result.append(f"{pezzi} di monete da €{banconota}")
        return " , ".join(result)

class PagamentoCartaDiCredito(Pagamento):
    def __init__(self,importo : float , nomeTitolareCarta : str , dataDiScadenza: float , numeroCartaDiCredito : int ):
        super().__init__()
        self.set_pagamento(importo)
        self.nomeTitolareCarta = nomeTitolareCarta
        self.dataDiScadenza = dataDiScadenza
        self.numeroCartaDiCredito = numeroCartaDiCredito

    def dettagli_pagamento(self):
        return (f"Il pagamento è di €{self.get_pagamento()} con carta di credito.\n " 
                f"Titolare: {self.nomeTitolareCarta}, Scadenza: {self.dataDiScadenza},\n "
                f"Numero Carta: {self.numeroCartaDiCredito}")
    


pagamento = Pagamento()

contanti1 = PagamentoContanti(150)
contanti2 = PagamentoContanti(95.25)
bancomat1 = PagamentoCartaDiCredito(200.00,"Mario Rossi","12/24",1234567890123456)
bancomat2 = PagamentoCartaDiCredito(500.00," Luigi Bianchi", "01/25" ,6543210987654321)

print(contanti1.dettagli_pagamento())
print(contanti1.inPezziDa())
print(contanti2.dettagli_pagamento())
print(contanti2.inPezziDa())
print(bancomat1.dettagli_pagamento())
print(bancomat2.dettagli_pagamento())
