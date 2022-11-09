# Chapter 6, Exercise 1: Pizza Toppings

toppings = []

while True:
    print("\n* Type 'quit' when you are done.") # A prompt so user would know to enter 'quit' when done with toppings
    topping = input("What toppings would you like on your pizza?: ")
    if topping != "quit":
        toppings.append(topping) # Adds the input to a list
    else:
        break
    print(f"  I'll add {topping} to your pizza.")

print(f"\nYou got a {', '.join(toppings)} pizza.") # Outputs a message that shows the toppings put in the toppings list