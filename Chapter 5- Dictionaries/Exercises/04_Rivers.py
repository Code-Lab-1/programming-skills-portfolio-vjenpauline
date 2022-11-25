# Chapter 5, Exercise 4: Rivers

rivers = {'Han':'Korea', 'Mekong':'Cambodia', 'Yangtze':'China'} # Dictionary of rivers and country they run through

for key, value in rivers.items():
    print(f"The {key} river runs through {value}.\n")

# Names of each river
print("Rivers:")
for key in rivers.keys(): 
    print(f"- {key}")

# Names of each country
print("\nCountries:")
for value in rivers.values():
    print(f"- {value}")
