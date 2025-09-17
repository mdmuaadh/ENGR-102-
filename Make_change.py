# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment"
#
# Names: 
# Jacob Gil
# Michael Mendoza
# Muaadh Mohideen
# Xander Tivis
# Section: ENGR - 102 - 559
# Assignment: Lab 4 Team project planner
# Date: 16-09-2025        

# This program will find how many an which coins are needed to be given as change    

from math import *

# gets input from user
pay = float(input("How much did you pay ($): "))
change = float(input("How much did it cost ($): "))
totalchange = pay - change

# checks to see if the amount should be paid in coins
if totalchange >= 1:
    print("\nThis amount should not be paid with coins")
    findcoins = round(totalchange * 100)
elif totalchange < 1 and totalchange > 0:
    findcoins = round(totalchange * 100)
else:
    print("\nThis amount should not be paid with coins")
    findcoins = int(totalchange)

quarters = findcoins // 25 # finds the amount of quarters needed 
findcoins %= 25 # finds the amount of change remaining after removing the amount of quarters
dimes = findcoins // 10 # finds the amount of dimes from remaining change
findcoins %= 10 # finds the amount of change remaining after removing the amount of dimes
nickels = findcoins // 5 # finds the amount of nickels from remaining change
findcoins %= 5 # finds the amount of change remaining after removing the amount of nickels
pennies = findcoins # gives the final amount of pennies

totalchange = round(totalchange,2)
# prints all of the quantities owed
print(f"\nYou should recieve a total of {totalchange} in the form of:\n{quarters} quarter(s)\n{dimes} dime(s)\n{nickels} nickel(s)\n{pennies} pennie(s)")



