#!/usr/bin/python3

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)

def convert_to_fahrenheit(celsius):
    return (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32

if __name__ == "__main__":
    value = float(input("Enter the temperature to convert: "))
    tem_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if tem_type == "F":
        result = convert_to_celsius(value)
        print(f"{value:.2f}°F is equal to {result:.2f}°C")

    elif tem_type == "C":
        result = convert_to_fahrenheit(value)
        print(f"{value:.2f}°C is equal to {result:.2f}°F")
    else:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
