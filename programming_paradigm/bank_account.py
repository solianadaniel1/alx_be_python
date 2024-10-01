#!/usr/bin/python3

class BankAccount:
    def init(self, account_balance= 0):
        self.account_balance = account_balance

    def deposit(self,amount):
        if amount > 0:
           self.account_balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: {self.account_balance}")
