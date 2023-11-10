#import math
from math import sqrt

xCoordinateArcher = float(input("x-coordinate of the archer "))
yCoordinateArcher = float(input("y-coordinate of the archer "))
xCoordinatePenguin = float(input("x-coordinate of the penguin "))
yCoordinatePenguin = float(input("y-coordinate of the penguin "))

xDistance = xCoordinatePenguin - xCoordinateArcher
yDistance = yCoordinatePenguin - yCoordinateArcher

print(f"{sqrt((xDistance**2)+(yDistance**2)):.2f}")
