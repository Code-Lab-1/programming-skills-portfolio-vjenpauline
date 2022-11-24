# Chapter 4, Exercise 10: Letters

# To check whether a letter is in a word
word = input("Give a word: ")
letter = input("Give a letter: ")

if letter in word:
    print(f"{letter} is in {word}.")
else:
    print(f"{letter} is not in {word}.")