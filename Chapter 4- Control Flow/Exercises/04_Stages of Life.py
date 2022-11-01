# Chapter 4, Exercise 4: Stages of Life

age = 101

if age < 2:
    print("The person is baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20: 
    print("The person is a teenager.")
elif age < 65:
    print("This person is an adult.")
else:
    print("This person is an elder.")

# or??? 

if age < 2:
    print("The person is baby.")
elif age >= 2 and age < 4:
    print("The person is a toddler.")
elif age >= 4 and age < 13:
    print("The person is a kid.")
elif age >= 13 and age < 20: 
    print("The person is a teenager.")
elif age >= 20 and age < 65:
    print("This person is an adult.")
else:
    print("This person is an elder.")