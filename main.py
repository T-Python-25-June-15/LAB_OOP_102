from bankAccount import BankAccount as Account

account1 = Account("Saif" , 5000)
account2 = Account("Abdullah" , 10000)
account3 = Account("Faisal" )



# Account 1
print(account1.get_account_holder())
print(account1.get_balance())
try:
    print(account1.withdraw(500))
except Exception as error:
    print(error)
try:
    print(account1.deposit(1000))
except Exception as error:
    print(error)
print()

# Account 2
print(account2.get_account_holder())
print(account2.get_balance())
try:
    print(account2.withdraw(2000))
except Exception as error:
    print(error)
try:
    print(account2.deposit(5000))
except Exception as error:
    print(error)
print()


# Account 3
print(account3.get_account_holder())
print(account3.get_balance())
try:
    print(account3.withdraw(2000))
except Exception as error:
    print(error)
try:
    print(account3.deposit(-5000))
except Exception as error:
    print(error)
print()