class BankAccount : 
    def __init__(self , account_holder : str , initial_balance :int = 0 ):
        
        self.__account_holder = account_holder
        self.__initial_balance = initial_balance
    
  
    def deposit(self , amount) :
        if amount <= 0:
            raise ValueError("Error : Deposit must be greater than zero.")
       
        self.__initial_balance = self.__initial_balance + amount
        return self.__initial_balance
    
    def withdraw (self , amount):
        if amount <= 0:
            raise ValueError("Error : Withdraw must be greater than zero.")
        if amount > self.__initial_balance:
            raise Exception("Insufficient funds.")
       
        self.__initial_balance = self.__initial_balance - amount
        return self.__initial_balance

    def get_balance(self): 
        return self.__initial_balance
    
    def get_account_holder(self):
        return self.__account_holder
  
    def set_balance(self , initial_balance):
        self.__initial_balance = initial_balance

    def set_account_holder(self , account_holder):
        self.__account_holder = account_holder
