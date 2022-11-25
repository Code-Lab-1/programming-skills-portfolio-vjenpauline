# Chapter 1, Exercise 5: Compute Area of Circle

import math

radius = float(input("What is the radius of the circle?: ")) # Asks user for radius to compute area of circle
area_circle = math.pi*(radius**2)

print(f"The area of the circle is {area_circle}.")