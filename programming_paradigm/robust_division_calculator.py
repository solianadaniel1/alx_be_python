#!/usr/bin/python3

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        dem = float(denominator)
        x = num/dem
        return f"The result of the division is {x}"
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print(" Please enter numeric values only.")
