# Chapter 7, Exercise 9: Basic Operations

def operations(a, b):
    # Sum: adds a and b, diff: subtracts a and b, product: multiplies a and b, div: divides a and b then prints
    sum = a + b
    diff = a - b
    product = a*b
    div = a/b

    print(f"Numbers {a} and {b}:")
    print(f"\tAdding the two will result {sum}.")
    print(f"\tSubtracting the two will result {diff}.")
    print(f"\tMultiplying the two will result {product}.")
    print(f"\tDividing the two will result {div}.")

operations(6, 12)
operations(20, 5)