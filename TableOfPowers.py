#initialize variables
mInput = 0
nInput = 0
pInput = 0


# Get user inputs
mInput = int(input("Input M: "))
nInput = int(input("Input N: "))
pInput = int(input("Input P: "))
stringDisplay = ""

#for loop for base range is from minput to ninput
for base in range(mInput, nInput+1, 1) :
    #for loop for power range is from 2 to pinput
    for power in range(2,pInput+1,1) :
        if power == 2 :
            # first entry without comma
            stringDisplay = str(base**power)
        else :
            stringDisplay = stringDisplay + ", " + str(base**power)
    print(f"{stringDisplay}")
