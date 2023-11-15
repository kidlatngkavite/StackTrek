from math import sqrt
coordinatesCounter  = 0
xInput = 0
yInput = 0
xCoordinateStart = 0
yCoordinateStart = 0
xCoordinatePrevious = 0
yCoordinatePrevious = 0
xCoordinateStop = 0
yCoordinateStop = 0
perimeter = 0
area = 0

while True:
    coordinatesCounter  += 1
    xInput = input(f"x{coordinatesCounter}: ")
    if xInput == "stop" :
        break
    yInput = input(f"y{coordinatesCounter}: ")
    if coordinatesCounter == 1 :
        xCoordinateStart = int(xInput)
        yCoordinateStart = int(yInput)
        xCoordinatePrevious = int(xInput)
        yCoordinatePrevious = int(yInput)
        continue
    else :
        #compute perimeter        
        xDistance = xCoordinatePrevious - int(xInput)
        yDistance = yCoordinatePrevious - int(yInput)
        perimeter += sqrt(xDistance**2 + yDistance**2)      

        #compute area
        area += (xCoordinatePrevious * int(yInput)) - (yCoordinatePrevious * int(xInput))


        #change variables for the next loop
        xCoordinatePrevious = int(xInput)
        yCoordinatePrevious = int(yInput)
        xCoordinateStop = int(xInput)
        yCoordinateStop = int(yInput)


#compute last side of perimeter        
xDistance = xCoordinateStop - xCoordinateStart
yDistance = yCoordinateStop - yCoordinateStart
perimeter += sqrt(xDistance**2 + yDistance**2)
print(f"Perimeter: {perimeter:.2f}")

#compute area with last side
area = abs((area + ((xCoordinatePrevious * yCoordinateStart) - (yCoordinatePrevious * xCoordinateStart)))/2)
print(f"Area: {area:.2f}")
        

    
