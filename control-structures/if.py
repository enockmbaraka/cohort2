#!/usr/bin/python3

"""Conditional statements"""
print("===if statements===")

# if statement
n = 10
if n >= 0:
    print("The number is positive: ", n)

# if-else statement
m = 5
if m >= 0:
    print("m is positive: ", m)
else:
    print("m is negative: ", m)
# getting input from the user
x = int(input("Enter the value of x: "))
if x >= 0:
    print("The value of x is postive: ", x)
else:
    print("The value of x is negative: ", x)

# if-elif-else statements
grade = 90
if grade > 90:
    print("You passed with flying colors!: ", grade)
elif grade == 90:
    print("Very good.Keep it up!: ", grade)
else:
    print("Pull up your socks!: ", grade)

# getting input from the user
g = int(input("Enter you grade: "))
if g > 90:
    print("You passed with flying colors!: ", g)
elif g == 90:
    print("Very good.keep it up!: ", g)
else:
    print("Pull up your socks!: ", g)
