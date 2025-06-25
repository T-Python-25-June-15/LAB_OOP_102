from bankAccount import BankAccount

bank1 = BankAccount("Naif Alghamdi", 1200)
bank1.menu()
option = input("Please enter the needed option: and 0 to exit: ")

while option != '0':
      match option:
             case '1':
                      bank1.deposit(200)
             case '2':
                      bank1.withdraw(1000)
             case '3':
                      print(bank1.get_balance())
             case '4':
                      print(bank1.get_account_holder())
             case _:
                      print("Invalid input")
      bank1.menu()
      option = input("Please enter the needed option: and 0 to exit: ")
print("Thank you for using our service, goodbye")





