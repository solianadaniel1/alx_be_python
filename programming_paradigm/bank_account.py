#!/usr/bin/python3

class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return f"Deposited: ${amount}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return f"Withdrew: ${amount}"
        return "Insufficient funds or invalid amount"

    def display_balance(self):
        return f"Current Balance: ${amount}"

