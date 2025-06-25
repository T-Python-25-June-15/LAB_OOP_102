from BankAccount import BankAccount as Bank




account1 = Bank("Abdulaziz", 1000000)
account2 = Bank("Ali")


print( f"{account1.get_account_holder()} your account balance: {account1.get_balance()}")
print( f"{account2.get_account_holder()} your account balance: {account2.get_balance()}")
print("-"*30)
account1.withdraw(500000)
print( f"{account1.get_account_holder()} your account balance: {account1.get_balance()}")
print("-"*30)

account2.deposit(500000)
print( f"{account2.get_account_holder()} your account balance: {account2.get_balance()}")


account2.deposit(-11)


