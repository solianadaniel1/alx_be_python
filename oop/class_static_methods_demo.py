#!/usr/bin/python3

class Calculator:
    calculation_type = "Arthimetic Operations"

    @staticmethod
    def add(a, b):
        return a + b
    @classmethod
    def multiply(cls, a, b):
        print(f"Calcualtion type: {cls.calculation_type}")
        return a * b
