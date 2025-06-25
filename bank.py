class BankAccount:

    def __init__(self,account_holder:str,initial_balance:float = 0) -> None:
        # Validate name & initial blance
        if not isinstance(account_holder,str):
            raise Exception ("Acocount holder name must be string")
        if not isinstance(initial_balance,float):
            raise Exception ("Balance must be positive number")
        
        self.account_holder = account_holder
        self.__initial_blance = initial_balance

    # Deposit method 
    def deposit(self,amount:float)-> float:
        # Validation
        if not isinstance(amount,(int,float)):
           raise Exception("Amount must be number")
        if amount <= 0:
            raise Exception("Amount must be positive")
        # Deposit opration
        self.__initial_blance += amount
        return self.__initial_blance
    
    # Withdraw method 
    def withdraw(self,amount)-> int:
        # Validation
        if not isinstance(amount,(int,float)):
           raise Exception("Amount must be number")
        elif amount > self.__initial_blance:
           raise Exception("Balance does not allow")
        # Withdraw opration
        self.__initial_blance -= amount
        return self.__initial_blance
           
    # getter method for return blance
    def get_balance(self) -> float:
        return self.__initial_blance
    
    # getter method for return account holder name
    def get_account_holder(self) -> str:
        return (self.account_holder)
    



