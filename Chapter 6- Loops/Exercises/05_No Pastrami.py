# Chapter 6, Exercise 5: No Pastrami

sandwich_orders = ["bologna", "pastrami", "caprese", "pastrami", "bagel", "peanut butter and jelly", "pastrami", "BLT"]
finished_sandwiches = []

print("Oh no! The deli has ran out of pastrami.")
out = "pastrami"
while out in sandwich_orders: # Removes pastrami from the sandwich orders list
    sandwich_orders.remove(out)

print("\nThank you for choosing the deli:")
while sandwich_orders: # Prints a message for each sandwich order, adds the sandwich to the list of finished orders
    order = sandwich_orders.pop()
    print(f"\tI am now making your {order} sandwich.")
    finished_sandwiches.append(order)

print("\nThank you for waiting:")
for i in finished_sandwiches: # Prints that the sandwich is now made
    print(f"\tYour {i} sandwich is made.")