# Chapter 2, Exercise 6: Investment

# Asks user for amount of money and time for a bank investment plan
savings = int(input("How much do you have now?: "))
years = int(input("How many years will it take?: "))
multiplier = 1.1
result = int(savings*(multiplier**(years)))

print(f"With ${savings} in the bank, you will end up with ${result} in {years} years.")