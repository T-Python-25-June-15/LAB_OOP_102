class BankAccount:
    def __init__(self,account_holder,initial_balance=0):
        self.account_holder = self.set_account_holder(account_holder)
        self.initial_balance = self.set_balance(initial_balance)
    
    def deposit(self,amount):
        self.initial_balance += amount
        return self.initial_balance
    def withdraw(self, amount):
        if self.initial_balance < amount:
            raise Exception("Your balance is less than the amount!")
        self.initial_balance -= amount
        return self.initial_balance
    def set_account_holder(self,account_holder):
        if account_holder == "":
            raise Exception("You need to enter a account name!")
        elif not isinstance(account_holder,str):
            raise Exception("The name need to be string!")
        else:
            return account_holder

    def set_balance(self,initial_balance):
        if not isinstance(initial_balance,int):
            raise Exception("The name need to be int!")
        else:
            return initial_balance
    def get_balance(self):
        return self.initial_balance
    def get_account_holder(self):
        return self.account_holder
    

    
        