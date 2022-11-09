# Chapter 6, Exercise 5: No Pastrami

# Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all
# occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ["bologna", "pastrami", "caprese", "pastrami", "bagel", "peanut butter and jelly", "pastrami", "BLT"]
finished_sandwiches = []

print("Oh no! The deli has ran out of pastrami.")
out = "pastrami"
while out in sandwich_orders:
    sandwich_orders.remove(out)

print("\nThank you for choosing the deli:")
while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"\tI am now making your {order} sandwich.")
    finished_sandwiches.append(order)

print("\nThank you for waiting:")
for i in finished_sandwiches:
    print(f"\tYour {i} sandwich is made.")

