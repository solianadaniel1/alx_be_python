#!/usr/bin/python3

# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    return (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32

if __name__ == "__main__":
    try:
        # User Input
        value = float(input("Enter the temperature to convert: "))  # Input for temperature
        temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()  # Input for type
        
        # Validation of temperature type
        if temp_type == "F":
            result = convert_to_celsius(value)
            print(f"{value}°F is {result:.10f}°C")  # Display converted temperature
        elif temp_type == "C":
            result = convert_to_fahrenheit(value)
            print(f"{value}°C is {result:.10f}°F")  # Display converted temperature
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

