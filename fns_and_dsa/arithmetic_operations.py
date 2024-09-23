#!/usr/bin/python3

def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            print("Division by zero is forbidden!!!")
        else:
            x = num1 / num2
    else:
        print("It is not correct try again")
