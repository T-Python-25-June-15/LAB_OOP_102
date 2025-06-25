class BankAccount:

    
    def __init__(self, account_holder, initial_balance = 0):
        self.account_holder = account_holder

        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__balance = initial_balance  

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be greater than zero.")
        if amount > self.__balance:
            raise Exception("Not enough balance.")
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance

    def get_account_holder(self):
        return self.account_holder


