# CHapter 3, Exercise 7: Seeing the World

places = ["Budapest", "Cappadocia", "Amsterdam", "Crete", "Venice", "Salzburg", "Switzerland", "Barcelona"]

print("Original list:")
print(places) # Initial arrangement

print("\nAlphabetically sorted list:")
print(sorted(places))

print("\nOriginal list:")
print(places)

print("\nAlphabetically sorted list in reverse:")
sorted(places, reverse=True)

print("\nOriginal list:")
print(places)

places.reverse()
print("\nOriginal list reversed:")
print(places)

places.reverse()
print("\nBack to original list:")
print(places)

places.sort()
print("\nAlphabetically sorted list again:")
print(places)

places.sort(reverse=True)
print("\nAlphabetically sorted list in reverse again:")
print(places)