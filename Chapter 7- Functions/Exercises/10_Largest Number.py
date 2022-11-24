# Chapter 7, Exercise 10: Largest Number

def largest(a,b,c): # Outputs the largest number from three
    if a >= b and a >= c:
        print(f"{a} is the largest number.")
    elif b >= a and b >= c:
        print(f"{b} is the largest number.")
    else:
        print(f"{c} is the largest number.")

largest(8,24,16)
largest(3,1,2)
largest(8,9,10)