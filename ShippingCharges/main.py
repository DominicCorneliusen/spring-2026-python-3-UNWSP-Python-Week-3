#Title: Shipping Charges
#Author: Dominic Corneliusen
#Date last modified: 2/4/2026

#Code Start

#Variables
userOrderWeightInPounds = float(input("Insert your order weight in pounds here: "))
weight = userOrderWeightInPounds

#Print Statements
if weight <= 0:
    print("Sorry, but your order weight is invalid. Please try again.")
elif weight <= 2:
    price = weight * 1.50
    print("Your order weight is",weight,". The price of your order is ",price,".")
elif 2 < weight <= 6:
    price = weight * 3.00
    print("Your order weight is",weight,". The price of your order is ",price,".")
elif 6 < weight <= 10:
    price = weight * 4.00
    print("Your order weight is",weight,". The price of your order is ",price,".")
else:
    price = weight * 4.75
    print("Your order weight is",weight,". The price of your order is ",price,".")