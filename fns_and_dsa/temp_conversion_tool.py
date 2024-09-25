#!/usr/bin/python3

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) +32

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit == 'C':
            convert_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}C is {converted_temp}F")
        elif unit == 'F':
            convert_temp = convert_to_celsius(temperature)
            print(f"{temperature}F is {convertes_temp}C")
        else:
            raise ValueError("Invalid unit. Pleae enter 'C' for celsius or 'F' for fahrenheit")
    except ValueError as e:
        print(f"Invalid Input:{e}")

if __name__ == "__main__":
    main()
