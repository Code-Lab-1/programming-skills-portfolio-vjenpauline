# Chapter 6, Exercise 8: Asking Dessert

favs = []
dessert = str(input('Do you like desserts?: '))

# Asks for the user's favorite desserts and adds them to the list of favs
while dessert != "quit":
    dessert = str(input('What are your favorite desserts?: '))
    if dessert != "quit":
        favs.append(dessert)

print(f"Your favorite desserts are: {favs}")