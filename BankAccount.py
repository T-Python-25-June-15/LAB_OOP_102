class BankAccount:

    def __init__(self, account_holder:str,initial_balance:int = 0):
        self.__account_holder=account_holder
        self.__initial_balance= initial_balance


    def deposit(self,amount:int):
        self.__initial_balance+= amount
        return self.__initial_balance
    
    def withdraw(self,amount:int):
        if(self.__initial_balance < amount):
            raise Exception("there is no balance in account")

        self.__initial_balance-=amount


    def get_balance(self):
        return self.__initial_balance
    
    def get_account_holder(self):
        return self.__account_holder
        