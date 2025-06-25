class BankAccount :

    
    def __init__(self , account_holder , balance = 0 ):
        self.__account_holder = account_holder
        if balance < 0:
             raise ValueError("Balance can not be negative!")
        self.__balance = balance
        

    # Method to add to the balance.
    def deposit (self , amount):
        if amount <= 0:
             raise ValueError("Deposit must be positive!")
        self.__balance = self.__balance + amount
        return self.__balance
    
    # Method to get the balance.
    def get_balance (self):
        return self.__balance
    
    # Method to withdraw amount.
    def withdraw(self , amount):
            if amount <= 0:
                 raise ValueError("Withdraw must be positive")
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
                return self.__balance
            else:
                 raise Exception ("Insufficient funds.")
    
    # Method to get account holder.
    def get_account_holder (self):
         return self.__account_holder
        
        
