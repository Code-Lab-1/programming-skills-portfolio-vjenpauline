# Chapter 5, Exercise 5: Pets

# Dictionary of different pets
pets = [
    {'Name':'Kiri',
    'Animal':'Dog',
    'Breed':'Shih Tzu',
    'Color/s':'Black and White',
    'Owner':'Pauline'},
    {
    'Name':'Luna',
    'Animal':'Dog',
    'Breed':'Maltese',
    'Color/s':'White',
    'Owner':'Maxine'},
    {
    'Name':'Barbie',
    'Animal':'Cat',
    'Breed':'Siamese',
    'Color/s':'White',
    'Owner':'Carmela'},
    {
    'Name':'Elsa',
    'Animal':'Chicken',
    'Breed':'Silkie Bantam',
    'Color/s':'White',
    'Owner':'Kylie',}
]

# Outputs everything known about the pets
for element in pets:
    print(f"\nEverything known about {element['Name']}:")
    for key, value in element.items():
        print(f"\t {key}: {value}")