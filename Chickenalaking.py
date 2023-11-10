import math
GRAVITY = 9.81
v0 = float(input("initial velocity "))
degrees = float(input("angle in degrees "))
time = float(input("time "))

xcoordinate = v0*math.cos(math.radians(degrees))*time
ycoordinate = (v0*math.sin(math.radians(degrees))*time)-(0.5*GRAVITY*(time**2))

print(f"{xcoordinate:.0f}, {ycoordinate:.0f}")