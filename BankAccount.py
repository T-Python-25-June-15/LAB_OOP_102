class BankAccount():
    def __init__(self , account_holder:str , initial_balance = 0 ):
        self.__account_holder = account_holder
        self.__initial_balance = initial_balance



    def deposit(self,amount:float):
        self.__initial_balance = amount + self.__initial_balance 
        return f"amount add: {amount}\ncurrent balance: {self.__initial_balance}"

    def withdraw(self,amount:float) :
      
      if amount < self.__initial_balance:
         self.__initial_balance = self.__initial_balance - amount  
         return f"withdraw ammount: {amount}\ncurrent balance:{self.__initial_balance}"
      else:
         raise Exception("the balance is not enough")
    
    def get_balance(self):
       return f"your balance:{self.__initial_balance}"

    def get_account_holder(self) :
       return f"account holder name:{self.__account_holder}"
      
