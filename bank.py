class BankAccount:
    def __init__(self,name, initial_balance=0):
        self.name = name
        if initial_balance < 0:
            print("initial balance is wrong ")
            initial_balance=0
        self.initial_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.initial_balance =self.initial_balance + amount
            return self.initial_balance
        else:
            print("error!")

    def withdraw(self, amount):
        if amount> self.initial_balance:
            raise Exception("not enough money")
        else:
            self.initial_balance = self.initial_balance - amount
            return self.initial_balance
        
    def get_balance(self):
        return self.initial_balance
    def get_account_holder(self):
        return self.name