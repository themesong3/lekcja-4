bmi = lambda h, w: w/((h/100)**2)
h = float(input("What is your height (cm) "))
w = float(input("What is your weight (kg) "))

print(bmi(h, w))