#Title: Age Classifier Program
#Author: Dominic Corneliusen
#Date Last modified: 2/3/2026

#Variables
Userage = int(input("Enter your age here:"))

if Userage <= 1 and Userage >= 0:
    print("You are an Infant")
elif Userage > 1 and Userage <13:
    print("You are a Child")
elif Userage >= 13 and Userage <20:
    print("You are a teenager")
elif Userage >= 20:
    print("You are an Adult")
    if Userage > 120:
        print("You are an adult. How are you still alive?")
else:
    print("Your age is invalid.")