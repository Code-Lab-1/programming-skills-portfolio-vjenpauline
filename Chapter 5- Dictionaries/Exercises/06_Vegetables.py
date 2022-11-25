# Chapter 5, Exercise 6: Vegetables

veg_list = {'Corn':'Yellow', 'Carrots':'Orange', 'Eggplant':'Purple'}

veg = str(input("Enter a vegetable: "))

# Checks if the user's input is a key
if veg in veg_list:
    print(f"{veg} is in the list.")
else:
    print("Give a different vegetable.")