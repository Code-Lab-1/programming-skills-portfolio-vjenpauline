# Chapter 6, Exercise 10: Range

# To enter a number and check if it is valid (between 0-9)
enter = True
while enter:
    num = int(input("Enter a number between 0 and 9: "))
    if num <= 9:
        enter = False
    else:
        print(f"""{num} is invalid.
        Only numbers between 0 and 9 are allowed.
        Enter a different number.""")

print(f"{num} is a valid number.")