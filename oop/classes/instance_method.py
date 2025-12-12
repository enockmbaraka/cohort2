#!/usr/bin/python3

class BankAccount:
    def __init__(self, acc_holder, balance=0):
        self.acc_holder = acc_holder
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt
        print(f"{self.acc_holder} deposited {amt} and the current balance is {self.balance}.")

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
            print("{} withdrew {} from her account and the current balance is {}".format(self.acc_holder, amt, self.balance))
        else:
            print("You account has insufficient funds.")


# creating an object
holder = input("What's your name: ?")
depo = int(input("Enter the amount you want to deposit: "))
withd = int(input("Enter the amount you want to withdraw: "))
bal = int(input("Enter your initial account balance: "))

bank = BankAccount(holder, bal)

# Accessing attributes of the object
print(bank.acc_holder)
print(bank.balance)
# calling the methods
bank.deposit(depo)
bank.withdraw(withd)
