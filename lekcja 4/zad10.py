import re


def read_number():
    x = int(input("Write a number "))
    return x

x = read_number()
y = read_number()

print(f"The sum is: {x+y}")