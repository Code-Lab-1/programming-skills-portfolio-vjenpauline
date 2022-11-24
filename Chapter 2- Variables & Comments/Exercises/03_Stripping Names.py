# Chapter 2, Exercise 3: Stripping Names

blonde = "\t \t \t Marilyn Monroe \n \n \n"
print(blonde)

print(blonde.lstrip()) # Removes whitespace at the beginning
print(blonde.rstrip()) # Removes trailing whitespace
print(blonde.strip()) # To remove all whitespace