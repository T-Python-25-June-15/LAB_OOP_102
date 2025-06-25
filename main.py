from BankAccount import BankAccount

user1 = BankAccount("nasser" , 500)
print(user1.deposit(300))
print("")
print(user1.withdraw(100))
print(user1.get_account_holder())
print(user1.get_balance())
