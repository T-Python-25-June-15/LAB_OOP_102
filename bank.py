class BankAccount:
    def __init__(self,account_holder,initial_balance=0):
        self.set_account_holder(account_holder)
        self.set_balance(initial_balance)
    
    def deposit(self,amount):
        self.__initial_balance += amount
        return self.__initial_balance
    def withdraw(self, amount):
        if self.__initial_balance < amount:
            raise Exception("Your balance is less than the amount!")
        self.__initial_balance -= amount
        return self.__initial_balance
    def set_account_holder(self,account_holder):
        if account_holder == "":
            raise Exception("You need to enter a account name!")
        elif not isinstance(account_holder,str):
            raise Exception("The name need to be string!")
        self.account_holder = account_holder

    def set_balance(self,initial_balance):
        if not isinstance(initial_balance,int):
            raise Exception("The name need to be int!")
        self.__initial_balance = initial_balance
    def get_balance(self):
        return self.__initial_balance
    def get_account_holder(self):
        return self.account_holder
    

    
        