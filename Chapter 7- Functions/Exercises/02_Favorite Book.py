# Chapter 7, Exercise 2: Favorite Book

def favorite_book(title): # Accepts a parameter (title) and prints a message using it
    msg = "One of my favorite books is "
    print(msg + title.title() + ".")

favorite_book("lolita")