# Chapter 5, Exercise 2: Glossary 1

glossary = {'Pseudocode':'describes the steps to an algorithm without a specific syntax', 
'Float':'stores a decimal number', 
'Function':'a reusable unit of code assigned to a fixed task', 
'Index':'addresses elements of an ordered series', 
'Docstring':'a string literal to explain functions, classes, etc.'}

print(glossary)

for key, value in glossary.items():
    
    print(f"{key}: {value} \n")