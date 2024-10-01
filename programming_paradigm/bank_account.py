#!/usr/bin/python3

class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance

    def deposit(self,amount):
        if amount >0:
            self.account_balance += amount
        else:
            return "Enter valid amount"
    def withdraw(self, amount):
        if amount > 0 and amount > self.account_balance:
            self.account_balance -=amount
        else:
            return "Insufficient balance"
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

