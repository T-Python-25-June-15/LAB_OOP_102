#Luluh Almogbil
'''
# LAB_OOP_102


Create a Python class called `BankAccount` that simulates a simple bank account. The class should have the following functionalities:

1. It should have a constructor that accepts the `account_holder` name and initial balance (`initial_balance`), setting the balance to zero if the initial balance is not provided.
2. A method called `deposit` that accepts an amount and adds it to the account balance, and then returns the updated balance.
3. A method called `withdraw` that accepts an amount and subtracts it from the account balance, returning the updated balance, 
but only if there are sufficient funds in the account.
If there are insufficient funds, it should raise an Exception and leave the balance unchanged (make sure to handle the exception when calling the method).
4. A method called `get_balance` that returns the current account balance.
5. A method called `get_account_holder` that returns the name of the account holder.

**NOTE:**
- Do validation, and other OOP principles as needed. 
- arrange your code in at least 2 files.

---------
'''

class BankAccount:
    
    #constructor
    def __init__(self, account_holder:str, initial_balance=0) -> None:# to identify or give an intial value to zero
        self.account_holder = account_holder
        self.set_balance(initial_balance) #private,encapsulating the attribute
        
    #setter   
    def set_balance(self,initial_balance):#will write to my balance
        if not isinstance(initial_balance,int):
            raise Exception("Balance must be a number dear")
        self.__initial_balance = initial_balance
    #getter   
    def get_balance(self):# will print and show my balance
        return self.__initial_balance   
    
    # def __connect_to_databse():
    #     pass
        
    def deposit(self,amount):
        self.set_balance(self.get_balance() + amount) 
        #account_Tbalance = self.initial_balance
        return self.get_balance()
    
    def withdraw(self,amount):
        
        if self.get_balance() >= amount:# do the withdraw operation
            self.set_balance(self.get_balance() - amount) 
            return self.get_balance()
        else:
            raise Exception("The withdraw operation cant be done .Your account doesnt hold that amount")
        
    def get_account_holder(self):
        return self.account_holder    
 
# #objects   
# client1 = BankAccount("Luluh",10000)

# print(client1.deposit(1000))
# print(client1.withdraw(6000))
# print(client1.get_balance())
# print(client1.get_account_holder())
