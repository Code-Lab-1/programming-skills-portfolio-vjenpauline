# Chapter 4, Exercise 7: BMI Calculator

# Asks user for their weight and height before calculating the BMI
weight = int(input("What is your weight?: "))
height = int(input("What is your height?: "))

BMI = (weight/(height**2))

# Displays their BMI ranking
if BMI < 18.5:
    print(f"You are underweight.")
elif BMI >= 18.5 and BMI < 25:
    print(f"You are healthy.")
elif BMI >= 25 and BMI < 30:
    print(f"You are overweight.")
elif BMI >= 30:
    print(f"You are obese.")