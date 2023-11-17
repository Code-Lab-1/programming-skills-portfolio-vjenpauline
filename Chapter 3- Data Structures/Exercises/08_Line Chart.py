# Chapter 3, Exercise 8: Line Chart

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,2,3,4,5]

# Creates a diagonal line chart with x and y coordinates list
plt.plot(x,y)

plt.title("This is an acceleration line graph.")
plt.xlabel("Time")
plt.ylabel("Acceleration")
plt.show()