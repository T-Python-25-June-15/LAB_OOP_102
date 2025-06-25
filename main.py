from bank import BankAccount

account = BankAccount("Me", 1000)
print(account.deposit(1000))
print(account.withdraw(500))
print(account.get_balance())
print(account.get_account_holder())
print()
print("-"*15)

account2 = BankAccount("me", )
print(account2.deposit(1000))
print(account2.withdraw(500))
print(account2.get_balance())
print(account2.get_account_holder())