# Chapter 6, Exercise 6: Adulthood

# Adds +1 to age until 60, continues when it hits the age of 40
age = 18
while age < 60:
    age += 1
    if age == 40:
        print("You are middle aged!")
        continue
    print(age)

print("Congrats on being a senior citizen!")