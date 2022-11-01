# CHapter 3, Exercise 6: Shrinking Guest List

guests = ["Julie Andrews", "Audrey Hepburn", "Danny DeVito", "Morgan Freeman"]

inv = ", I am inviting you to a Thanksgiving dinner at my place."

print(guests[0] + inv)
print(guests[1] + inv)
print(guests[2] + inv)
print(guests[3] + inv)

print("\n \t" + guests[1] + " can't make it.\n") # Outputs message that shows guest can't come

guests[1] = "Arnold Schwarzenegger" # Replaces with a new person

print(guests[0] + inv)
print(guests[1] + inv)
print(guests[2] + inv)
print(guests[3] + inv)

print("\n \t" + "I apologize. My new dinner table won't arrive in time. I can only invite two people for dinner.") 
# Outputs message that only 2 people can come

name = guests.pop() # Removes person from guest list
print("\n" + "Sorry " + name + ", I can't invite you to dinner.")
name = guests.pop()
print("Sorry " + name + ", I can't invite you to dinner.")

# Sends a message to the two people left on the list
print(guests[0] + ", you're still invited to the dinner.")
print(guests[1] + ", you're still invited to the dinner.")

del guests[:] # Clears the guests list (removes the 2 people left)

print(guests)