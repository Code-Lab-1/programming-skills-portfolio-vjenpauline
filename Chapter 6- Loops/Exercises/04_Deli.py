# Chapter 6, Exercise 4: Deli

sandwich_orders = ["bologna", "caprese", "bagel", "peanut butter and jelly", "BLT"]
finished_sandwiches = []

print("Thank you for choosing the deli:")
while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"\tI am now making your {order} sandwich.")
    finished_sandwiches.append(order)

print("\nThank you for waiting:")
for i in finished_sandwiches:
    print(f"\tYour {i} sandwich is made.")