# Chapter 7, Exercise 7: List

fruits = ["apple", "banana", "mango", "plum", "strawberry"]
colors = ["red", "orange", "yellow", "green", "blue"]

def allnames(list): # Outputs elements of a list in one line each
    for i in list:
        print(i.title())

allnames(fruits)
allnames(colors)