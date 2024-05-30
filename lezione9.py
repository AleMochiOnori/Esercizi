
class Account:
    def __init__(self,  account_id , balance):
        self.account_id = account_id
        self.balance = balance



    def deposit(self , amount : float):
        amount += self.balance   

    def get_balance(self) :
        return self.balance
       

            
class Bank :
    def __init__(self , accounts : dict[str , Account]):
        self.accounts = accounts

    def create_account(self , account_id):
        self.accounts.add(account_id)
        print(self.accounts)
        self.balance = 0


    def deposit(self, account_id , amount ):
        if account_id == account_id :
            amount += self.balance

    def get_balance( self ,account_id) :
        return account_id       