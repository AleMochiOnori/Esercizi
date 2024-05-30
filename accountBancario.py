class ContoBancario :
    total_accounts = 0
    def __init__(self,saldo : int, iban : int, nome : str):
        self.saldo = saldo 
        self.nome = nome 
        self.iban = iban

        ContoBancario.total_accounts += 1


    def deposito(self,importo : int) :
        self.saldo += importo
        print(f"{importo} è stato aggiunto . Il nuovo saldo è {self.saldo}")



    def prelievo(self,importo : int):
        self.saldo -= importo
        print(f"{importo} è stato ritirato  . Il nuovo saldo è {self.saldo}")        




    @classmethod     
    def  total_Accounts(cls):
        print(f"{cls.total_accounts}")   

    @staticmethod
    def valida_account(iban : int):
        if isinstance(iban , int) and len(str(iban)) == 10: # type: ignore
            print("iban valido")
            return True
        else:
            print("iban non valido")
            return False
        

conto = ContoBancario(500 , "0123456789", "aldo")
conto.deposito(20)