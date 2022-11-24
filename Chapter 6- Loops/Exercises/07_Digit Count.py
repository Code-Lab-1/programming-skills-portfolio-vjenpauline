# Chapter 6, Exercise 7: Digit Count

# Checks the digit count of the user input
num = int(input("Give a number: "))
count = 0

while num != 0:
    num //= 10
    count += 1

print(f"It is with {count} digits.")