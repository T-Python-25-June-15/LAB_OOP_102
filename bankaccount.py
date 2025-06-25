
class BankAccount:
    def __init__(self,account_holder,initial_balance=0):
        self.__name = account_holder
        self.__balance = initial_balance

    def deposit(self,amount):
        if type(amount) is not int:
            raise ValueError("Only Integer values")

        self.__balance = self.__balance + amount

    def withdraw(self,amount):
        if type(amount) is not int:
            raise ValueError("Only Integer values")
        elif amount > self.__balance:
            raise ValueError("Thats more than what you have ")
        else:
            self.__balance = self.__balance - amount

        
    def get_balance(self):
        return self.__balance

    def get_account_holder(self):
        return self.__name