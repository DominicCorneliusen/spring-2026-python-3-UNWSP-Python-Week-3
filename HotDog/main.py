#Title: Hot Dog
#Author: Dominic Corneliusen
#Date last modified: 2/6/2026

#Start
#Input variables
hotDogType = input("Hello! What kind of hot dog would you like? (regular/chili dog)")
cheese = input("Would you like cheese? (yes/no) ")
pepper = input("Would you like peppers? (yes/no) ")
grilledOnion = input("Would you like grilled onions? (yes/no) ")
#if else statements
if hotDogType == "Regular" or hotDogType == "regular":
    price = 3.50
else:
    price = 4.50
if cheese == "yes":
    price = price + 0.50
if pepper == "yes":
    price = price + 0.75
if grilledOnion == "yes":
    price = price + 1.00
#Variables based on user input
tax = price * 0.07
total = price + tax
#print the final price, tax and overall cost of the order
print("Price of order:",price)
print("Tax:",tax)
print("Total cost:",total)
