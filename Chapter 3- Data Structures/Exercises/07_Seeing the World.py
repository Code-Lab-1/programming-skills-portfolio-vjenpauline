# CHapter 3, Exercise 7: Seeing the World

places = ["Budapest", "Cappadocia", "Amsterdam", "Crete", "Venice", "Salzburg", "Switzerland", "Barcelona"]

print("Original list:\n", places) # Initial arrangement

print("\nAlphabetically sorted list:\n", sorted(places))

print("\nOriginal list:\n", places)

print("\nAlphabetically sorted list in reverse:\n", sorted(places, reverse=True))

print("\nOriginal list:\n", places)

places.reverse()
print("\nOriginal list reversed:\n", places)

places.reverse()
print("\nBack to original list:\n", places)

places.sort()
print("\nAlphabetically sorted list again:\n", places)

places.sort(reverse=True)
print("\nAlphabetically sorted list in reverse again:\n", places)