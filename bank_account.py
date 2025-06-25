class BankAccount:
    def __init__(self, account_holder:str, initial_balance:float=0):
        self.__account_holder:str = account_holder
        self.set_balance(initial_balance)

    def deposit(self, amount:float):
        if amount > 0 and isinstance(amount, (int, float)):
            self.set_balance(self.__initial_balance + amount)
            return self.__initial_balance
        else:
            raise Exception("Enter a valid amount") 


    def withdraw(self, amount:float):
        if amount > 0 and isinstance(amount, (int, float)):
            if self.__initial_balance >= amount:
                self.set_balance(self.__initial_balance - amount)
                return self.__initial_balance
            else:
                raise Exception("Balance unchanged")
        else:
            raise Exception("Enter a valid amount")
        
    def get_balance(self):
        return self.__initial_balance
    
    def get_account_holder(self):
        return self.__account_holder

    def set_balance(self, new_balance:float):
        if isinstance(new_balance, (int, float)):
            self.__initial_balance:float = new_balance
        else:
            raise Exception("Enter a valid amount")
            