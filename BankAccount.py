'''
# LAB_OOP_102


Create a Python class called `BankAccount` that simulates a simple bank account. The class should have the following functionalities:

1. It should have a constructor that accepts the `account_holder` name and initial balance (`initial_balance`), setting the balance to zero if the initial balance is not provided.
2. A method called `deposit` that accepts an amount and adds it to the account balance, and then returns the updated balance.
3. A method called `withdraw` that accepts an amount and subtracts it from the account balance, returning the updated balance, but only if there are sufficient funds in the account. If there are insufficient funds, it should raise an Exception and leave the balance unchanged (make sure to handle the exception when calling the method).
4. A method called `get_balance` that returns the current account balance.
5. A method called `get_account_holder` that returns the name of the account holder.

**NOTE:**
- Do validation, and other OOP principles as needed. 
- arrange your code in at least 2 files.

---------
'''


class BankAccount:

    def __init__(self, account_holder: str ,initial_balance:int =0 ):
        self.set_account_holder(account_holder)
        self.__set_balance(initial_balance)




    def deposit(self, added_amount: int) -> int:
        if added_amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        new_amount = self.get_balance() + added_amount
        self.__set_balance(new_amount)
        return self.get_balance()


    def withdraw(self, withdraw_amount: int) -> int:
        if withdraw_amount <= 0:
            raise ValueError("Withdraw amount must be positive number")
        if self.get_balance() < withdraw_amount:
            raise Exception("Insufficient balance")
        
        new_amount = self.get_balance() - withdraw_amount
        self.__set_balance(new_amount)
        return self.get_balance()

            

        
#setters

    def __set_balance(self, amount: int):
        if amount < 0:
            raise ValueError("Balance cannot be negative nubere")
        
        self.__balance = amount




    def set_account_holder(self, account_holder: str):
        if not isinstance(account_holder, str):
            raise TypeError("Name must be a string")
        if len(account_holder.strip()) <= 2:
            raise ValueError("Name must be longer than 2 characters")
        
        self.__account_holder = account_holder


#getters
    def get_balance(self) -> int:
        return self.__balance
    

    def get_account_holder(self) -> str:
        return self.__account_holder
