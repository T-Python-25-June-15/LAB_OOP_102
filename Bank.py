class BankAccount:
    def __init__(self,account_holder,initial_balance):
       self.account_holder=account_holder
       self.__balance=initial_balance
       
    def deposit (self,amount):
        self.__balance+=amount
        return self.__balance
    def withdraw(self,amount):
        try:
           
            if amount<=self.__balance:
                self.__balance= self.__balance-amount
                return f"Balance after withdraw {self.__balance}"
            else:
                return"Insufficient"
            
        except:
            print("error")        

         

    def get_balance(self):
        return f"Balance {self.__balance} "
    
