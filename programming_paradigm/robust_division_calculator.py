#!/usr/bin/python3

def safe_divide(numerator, denominator):
    try:
        # Try converting inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Perform division
        result = numerator / denominator
        return f"Result: {result:.2f}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Non-numeric input provided."

