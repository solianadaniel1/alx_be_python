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
        if amount > 0 and amount <= self.account_balance:  # Ensure the amount is positive and does not exceed the balance
            self.account_balance -= amount
            return f"Withdrew: ${amount:.2f}"
        return "Insufficient funds."  # Correct error message when funds are insufficient

    def display_balance(self):
        return f"Current Balance: ${self.account_balance:}"  # Return current balance

