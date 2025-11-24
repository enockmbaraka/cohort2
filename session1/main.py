#!/usr/bin/python3

from calculator import add, sub, div, mul, exp

a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

print("Addition: ", add(a, b))
print("Subtraction: ", sub(a, b))
print("Multiplication: ", mul(a, b))
print("Divison: ", div(a, b))
print("Exponentation: ", exp(a, b))
print(add.__doc__)
print(sub.__doc__)
print(mul.__doc__)
# help(div)
# help(exp)
