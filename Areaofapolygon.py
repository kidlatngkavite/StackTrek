#import math
from math import radians, cos, sin

GRAVITY = 9.81
v0 = float(input("initial velocity "))
degrees = float(input("angle in degrees "))
time = float(input("time "))

xcoordinate = v0*cos(radians(degrees))*time
ycoordinate = (v0*sin(radians(degrees))*time)-(0.5*GRAVITY*(time**2))

print(f"{xcoordinate:.0f}, {ycoordinate:.0f}")