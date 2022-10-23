def isInRange(x, y, n):
    if n >= x and n <= y:
        return True
    else:
        return False

x = int(input("Write the opening number for range "))
y = int(input("Write the closing number for range "))
n = int(input("Give me a number (ill check if its in the range) "))