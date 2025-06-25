from BankAccount import BankAccount


bankAccount = BankAccount("meshari",10)
print("account placeholder: " + bankAccount.get_account_holder())
print("account balance: " + str(bankAccount.get_balance()))

try:
    print("account balance after deopsit 10 :" + str(bankAccount.deposit(30)))
except Exception as e:
    print(e)

print("new account balance: " + str(bankAccount.get_balance()))

try:
    print("account balance after withdraw 20 :" + str(bankAccount.withdraw(20)))
except Exception as e:
    print(e)

print("new account balance: " + str(bankAccount.get_balance()))


try:
    print("account balance after withdraw 30 :" + str(bankAccount.withdraw(30)))
except Exception as e:
    print(e)

print("new account balance: " + str(bankAccount.get_balance()))
