from classes import BankAccount


#object
client1 = BankAccount("Luluh",20000)



print("Current account balance is: ",client1.get_balance())
print("The updated balance after making a deposit is: ",client1.deposit(1000))
print("The updated balance after making a withdraw is: ",client1.withdraw(5000))
print("Current account balance is: ",client1.get_balance())
print("The account holder name is: ",client1.get_account_holder())
print("-"*53)

client1 = BankAccount("Mohammed",5000)
print("Current account balance is: ",client1.get_balance())
print("The updated balance after making a deposit is: ",client1.deposit(1000))
print("The updated balance after making a withdraw is: ",client1.withdraw(5000))
print("Current account balance is: ",client1.get_balance())
print("The account holder name is: ",client1.get_account_holder())
print("-"*53)