from classes import BankAccount

# Condition 01: no initial balance
try:
    account1 = BankAccount("Sarah") #create account with 0 as initial balance 
    account1.deposit(600.60)
    print(account1.get_info())
except Exception as e:
     print(e)

# Condition 02: deposit invalid input 
try:
    account2 = BankAccount("Maha",1000) 
    account2.deposit("hundred")
    print(account2.get_info())
except Exception as e:
     print(e)
     
# Condition 03: withdraw invalid input
try:
    account3 = BankAccount("Nada",3000) 
    account3.withdraw("5$")
    print(account3.get_info())
except Exception as e:
     print(e)
     
# Condition 04: deposit negative amount input  
try:
    account4 = BankAccount("Fatimah",3000) 
    account4.deposit(-100)
    print(account4.get_info())
except Exception as e:
     print(e)
     
# Condition 05: withdraw negative amount input 
try:
    account5 = BankAccount("Njood",7000) 
    account5.withdraw(-500)
    print(account5.get_info())
except Exception as e:
     print(e)
     
# Condition 06: withdraw amount, more than the current balance  
try:
    account6 = BankAccount("Mznh",100) 
    account6.withdraw(500)
    print(account6.get_info())
except Exception as e:
     print(e)