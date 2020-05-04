import time
import os

print("Welcome to the Timer Program")

Amount = input("Please enter the amount of minutes you want the timer to run for \n")

print("Alright so the timer is set to " + Amount + " Minutes Correct? \n")

Amount = int(Amount)

Verify = input("yes or no\n")

if Verify == "yes":
    print("timer counting down")
    Final_Amount = (Amount * 60)
    time.sleep(Final_Amount)
    os.system("aplay bell.wav&")
else:
    print("No, Okay just run me again...")
