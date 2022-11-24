# Chapter 7, Exercise 6: Within the Raange

def check(num, min, max): 
    # Checks whether number is within the range of two numbers
    if num >= min and num <= max:
        print(f"{num} is between {min} and {max}.")
    else:
        print(f"{num} is not between {min} and {max}.")

check(4, 2, 4)