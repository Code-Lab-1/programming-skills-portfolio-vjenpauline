# Chapter 7, Exercise 4: Large Shirts

def make_shirt(size = "large", msg = "I love Python"): 
    # Prints a statement with large as the default size and "I love Python" as the default message
    print(f"A {size}-sized shirt with '{msg}' printed on it will be made.\n")

make_shirt()
make_shirt("medium")
make_shirt("medium", "Put Your Head on My Shoulder")