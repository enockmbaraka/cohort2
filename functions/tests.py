#!/usr/bin/python3

from fact import factorial
x = int(input("Enter a number to get factorial: "))

fact = factorial(x)
print("The factorial of {} is:  {}".format(x, fact))
