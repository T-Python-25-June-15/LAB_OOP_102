

class BankAccount :
    
    def __init__(self, account_holder_name:str, initial_balabnce = 0):
        self.set_account_holder_name(account_holder_name)
        self.set_balance(initial_balabnce)

    def deposit(self, amount:int):
        if amount < 0:
            raise Exception("ERROR: Amount must be positive")
        self.set_balance(self.get_balance() + amount)
        return self.__balance
    
    def withdraw(self, amount:int):
        if amount < 0:
            raise Exception("ERROR: Amount must be positive")
        if self.__balance < amount:
            raise Exception(f"ERROR: Insufficient funds in the account, Your balance is: {self.__balance}")
        
        self.set_balance(self.get_balance() - amount)
        return self.__balance
    
    def set_balance(self, amount):
        if not isinstance(amount, int):
            raise Exception("ERROR: Balance must be integer")
        if amount < 0:
            raise Exception("ERROR: Amount must be positive")
        self.__balance = amount

    def set_account_holder_name(self, name):
        if not isinstance(name, str):
            raise Exception("ERROR: Name must be text")
        self.__account_holder_name = name


    def get_balance(self):
        return self.__balance
    
    def get_account_holder(self):
        return self.__account_holder_name