from Bank import BankAccount

a=BankAccount("lujain",88)
a.deposit(500)
print(a.withdraw(300))
print(f" {a.get_balance()}")
print(a.account_holder)
