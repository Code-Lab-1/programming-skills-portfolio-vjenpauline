# CHapter 3, Exercise 5: Change Guest List

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