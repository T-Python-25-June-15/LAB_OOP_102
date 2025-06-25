

class BankAccount:
    
    def __init__(self, account_holder:str, initial_balance:float = 0.0):
        self.__setAccountHolder(account_holder)
        self.__setBalance(initial_balance)
        
    def deposit(self, amount:float):
        self.__setBalance(amount + self.getBalance())
        return self.getBalance()
    
    def withdraw(self, amount:float):
        if amount > self.getBalance():
            raise Exception("You do not have enough credit")
        elif amount <= 0:
            raise Exception("positive number only")
        else:
            self.__setBalance(self.getBalance() - amount)
        return self.getBalance()
    
    # Getters and Setters
    def getBalance(self):
        return self.__balance
    
    def getAccountHolder(self):
        return self.__account_holder
    
    def __setAccountHolder(self, account_holder:str):
        if len(account_holder) < 2 or account_holder.isdigit():
            raise Exception("Invalied account holder, please try again")
        else:
            self.__account_holder = account_holder
            
    def __setBalance(self, balance:float):
        if isinstance(balance, float):
            self.__balance = balance
        else:
            raise Exception("Invaild balance, please try again")