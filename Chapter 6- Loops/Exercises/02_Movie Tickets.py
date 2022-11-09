# Chapter 6, Exercise 2: Movie Tickets

while True:
    print("\n* Type 'quit' when you are done.") # A prompt so user would know to enter 'quit' when done with checking costs
    age = input("How old are you?: ")
    if age == "quit":
        print("\nEnjoy the movie!")
        break

    age = int(age)
    
    if age < 3:
        cost = 0
    elif age <= 12:
        cost = 10
    else:
        cost = 15

    print(f"  Your ticket costs ${cost}.")

