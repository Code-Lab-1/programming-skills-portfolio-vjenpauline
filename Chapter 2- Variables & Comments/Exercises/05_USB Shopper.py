# Chapter 2, Exercise 5: USB Shopper

USBprice = 6
money = 50
USBamount = (money // USBprice) # Calculates how many USB sticks the girl can buy

print(USBamount)

change = (money - (USBamount*USBprice)) # Calculates how much money she'll have left

print("The girl will have", change, "pounds left.")
