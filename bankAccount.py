class BankAccount:
    account_holder:str
    init_balance:int

    def menu(self,):
        print("_"*20)
        print("Welcome to the Bank\nPlease select the needed option: ")
        print("(1).To deposit")
        print("(2).To withdraw")
        print("(3).To check the balance")
        print("(4).To display the account holder name")


    def __init__(self, account_holder:str, init_balance:int = 0):
        self.account_holder = account_holder
        self.init_balance = init_balance

    def deposit(self, deposit_amount:int):
        self.init_balance += deposit_amount
        print(f"--The amount of: {deposit_amount} was added successfully\n--the current balance is: {self.init_balance}")

    def withdraw(self, amount:int =0):
        try:
            if amount <= 0:
                print("--Amount must be positive")
                return
            if amount >= self.init_balance:
                self.init_balance - amount
                print(f"--Sorry your ammount not available, your current balance is: {self.init_balance}")
            else:
                self.init_balance -= amount
                print(f"--Amount was successfuly withdrawn\n--your current balance is: {self.init_balance}")
        except ValueError:
         print("--Error: Please enter a valid number")
    def get_balance(self):
        return f"--the current account balance is: {self.init_balance}"

    def get_account_holder(self):
        return f"--The name of the account holder is: {self.account_holder}"



    