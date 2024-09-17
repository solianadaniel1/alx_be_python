#!/usr/bin/python3

number = int(input("Enter the size of the pattern: "))
row = 0

while row < number:
    col = 0
    while col < number:
        print("*", end="")
        col += 1
    print()
    row += 1
