# Chapter 4, Exercise 6: Temperature

# Asks user for temperature of water and determines its temperature point
temp = int(input("What's the temperature?: "))
if temp >= 100:
    print(f"The temperature is boiling.")
elif temp == 0:
    print(f"The temperature is freezing.")
else:
    print("Other")