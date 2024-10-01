#!/usr/bin/python3

def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Perform the division
        result = numerator / denominator
        return f"Result: {result:.2f}"

    except ZeroDivisionError:
        return "Cannot divide by zero."

    except ValueError:
        return "Please enter numeric values only."

