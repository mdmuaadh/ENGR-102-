# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment"
#
# Names: 
# Jacob Gil
# Michael Mendoza
# Muaadh Mohideen (Project manager)
# Xander Tivis
# Section: ENGR - 102 - 559
# Assignment: Lab 6 Team project planner
# Date: 30-09-2025

from math import *

#gets the inputs from the user
sidelength = int(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))

#calculates the area of 1 cubes side
sidearea = sidelength ** 2

#defines rest of the variables used
total = 0
topfaces = 0
sidefaces = 0

for i in range(1, layers + 1):
    topfaces += (2 * i - 1) * sidearea #finds the area of all of the top facing sides
    sidefaces += 4 * i * sidearea #finds the area of all of the side facing sides
total = topfaces + sidefaces #finds the total area
print(f"You need {total:.2f} m^2 of gold foil to cover the pyramid") #prints the total area in the correct format
