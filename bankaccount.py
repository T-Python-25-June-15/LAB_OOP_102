

class BankAccount:
    def __init__(self, account_holder:str, initial_balance:float = 0):
        self.account_holder = account_holder
        self.__set_inital_balance(initial_balance)

    def __set_inital_balance(self, balance:float) -> None:
        if not isinstance(balance, (float, int)):
            raise Exception ("Please inter valid number")
        if balance < 0:
            raise Exception("your balance is lower then 0")
        self.__balance = balance

    def get_balance(self) -> float:
        print(f"your balance is :{self.__balance}$")
        return self.__balance
     
    
    def deposit(self, amount:float) -> float:
        new_balance = self.get_balance() + amount
        self.__set_inital_balance(new_balance)
        return self.get_balance()

    def withdraw(self, amount:float) -> float:
        new_balance = self.get_balance() - amount
        self.__set_inital_balance(new_balance)
        return self.get_balance()


    def get_account_holder(self):
        print(self.account_holder)