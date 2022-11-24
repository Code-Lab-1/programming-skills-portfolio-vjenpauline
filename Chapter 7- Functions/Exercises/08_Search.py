# Chapter 7, Exercise 8: Search

def search(x,y): # Searches if word(y) is in text(x)
    if y in x:
        return y
    else:
        return x

text = input()
word = input()

if (search(text, word) == word):
    print("Word found")
else:
    print("Word not found")