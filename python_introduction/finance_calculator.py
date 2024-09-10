#!/usr/bin/env python3

income = int(input("Enter your monthly income:"))
expense = int(input("Enter your monthly expenses:"))

monthly_savings = abs(expense - income)
savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${savings}")
