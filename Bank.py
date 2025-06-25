from BankAccount import BankAccount


account = BankAccount("Mohammed Jabbari", 1000)
Account = BankAccount("Ali Jabbari", 6500)


print("*************** BankAccount ***************")
print(f"account_holder : {account.get_account_holder()}") 
account.deposit(500) 
account.withdraw(2000) 


print("*************** BankAccount ***************")
print(f"account_holder : {Account.get_account_holder()}")
account.deposit(1500)
account.withdraw(360)