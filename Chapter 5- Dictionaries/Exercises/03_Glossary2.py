# Chapter 5, Exercise 3: Glossary 2

glossary = {
    'Pseudocode':'describes the steps to an algorithm without a specific syntax', 
    'Float':'stores a decimal number', 
    'Function':'a reusable unit of code assigned to a fixed task', 
    'Index':'addresses elements of an ordered series', 
    'Docstring':'a string literal to explain functions, classes, etc.',
    'Concanetation':'merging strings',
    'Algorithm':'steps to perform a task',
    'len() Function':'used to find length of an object',
    'print() Function':'used to print a message',
    'range() Function':'used to show a sequence of numbers' } # Dictionary of Python terms with 5 more additions

for key, value in glossary.items(): 
    print(f"{key} \n- {value} \n") # Outputs the word name(key) and its meaning(value) in an organized format with a loop