#!/usr/bin/python3

class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return f"Deposited: ${amount:.2f}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return f"Withdrew: ${amount:.2f}"
        return "Insufficient funds or invalid amount"

    def display_balance(self, amount):
        return f"Current Balance: ${self.amount:.2f}"

