# Chapter 5, Exercise 8: Fast Food

orders = {
    'Elon':'salad',
    'Steve':'apple pie',
    'William':'burger',
    'Jeff':'bacon and egg'
}

# Outputs the customer with their order of choice
for key, value in orders.items():
    print(f"{key}'s fast food order is {value}.")
    print(f"It is their favorite food.\n")

customers = ['Ariana', 'Jeff', 'Stefania', 'Simon', 'Elon', 'Taylor']

# Checks if the person has ordered or not. Outputs a statement if they have and if they have not.
for key in customers:
    if key in orders.keys():
        print(f"You have ordered successfully, {key}.")
    else:
        print(f"Welcome, {key}! What did you want to order?")