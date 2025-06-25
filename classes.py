class BankAccount:
    def __init__(self, account_holder:str, initial_balance:float = 0) -> None:
        self.__set_account_holder(account_holder)
        self.__set_balance(initial_balance)
        
        
    def deposit(self,amount:float) -> float:
        if isinstance(amount, (int,float)):
            if amount <= 0:
                raise Exception("Deposit amount must be greater than 0")
            else:
                self.__set_balance(self.__get_balance() + amount)
                return self.__get_balance() 
        else:
            raise Exception("Deposit amount must be an number.")
    
    def withdraw(self,amount:float) -> float:
        if isinstance(amount, (int,float)):
            if amount <= 0:
                raise Exception("Withdraw amount must be greater than 0")
            elif self.__get_balance() - amount < 0:
                raise Exception("Insufficient funds!")                
            else:     
                self.__set_balance(self.__get_balance() - amount)
                return self.__get_balance()   
        else:
            raise Exception("Withdraw amount must be an number.")

    # Balance - Setter
    def __set_balance(self, balance:float) -> None:
        self.__balance = balance
    
    # Balance - Getter
    def __get_balance(self) -> float:
        return self.__balance     
    
    
    # Holder - Setter 
    def __set_account_holder(self, account_holder:str) -> None:
        self.__account_holder = account_holder

    # Holder - Getter 
    def __get_account_holder(self) -> str:
        return self.__account_holder
    
    def get_info(self)-> None:
        return f"The balance of {self.__get_account_holder()} account is {self.__get_balance()}"