# Chapter 3, Exercise 9: Pie Chart

import matplotlib.pyplot as plt

sales = [8, 8, 9, 9, 11, 12, 12, 31]
sales_type = ["Other","Refirgeration","Appliances","Computers & Electronics", "Lighting", "Water Heating", "Space Cooling", "Space Heating"]

# Crates a pie chart with the values inside sales list
plt.pie(sales, labels = sales_type)
plt.title("This is a sales pie chart.")
plt.xlabel("Sales")
plt.show()