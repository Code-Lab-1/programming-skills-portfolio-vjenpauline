# Chapter 4, Exercise 8: Eligibility

# Asks for the user's age to determine eligibility to vote
age = int(input("How old are you?: "))

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")