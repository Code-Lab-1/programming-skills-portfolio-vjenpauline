# Chapter 4, Exercise 9: Prime Number

# Asks user for a number to determine whether it is a prime number or not
num = int(input("Check if a prime number: "))

if num > 1:
        for i in range(2, int(num/2)+1):
            if num%i == 0:
                print(f"{num} is not a prime number.")
                break
        else:
            print(f"{num} is a prime number.")