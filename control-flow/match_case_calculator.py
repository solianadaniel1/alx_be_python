#!/usr/bin/python3

# Prompt the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt the user for an operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using match-case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        print("Invalid operation. Please choose one of the following: +, -, *, /.")

