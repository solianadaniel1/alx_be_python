#!/usr/bin/env python3

income = int(input("Enter your monthly income:"))
expense = int(input("Enter your total monthly expenses:"))

monthly_savings = abs(expense - income)
savings = abs(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print(f"Your monthly savings are ${int(monthly_savings)}")
print(f"Projected savings after one year, with interest, is: ${int(savings)}")
