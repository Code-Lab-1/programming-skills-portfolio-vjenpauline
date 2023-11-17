# Chapter 2, Exercise 5: USB Shopper

usbprice = 6
money = 50
usbamount = (money // usbprice) # Calculates how many USB sticks the girl can buy

print(usbamount)

change = (money - (usbamount * usbprice)) # Calculates how much money she'll have left

print(f"The girl will have {change} pounds left.")
