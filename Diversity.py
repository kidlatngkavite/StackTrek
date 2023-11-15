#initialize varbiables
numberEnrolles = 0
counterMale = 0
counterFemale = 0
gcdinit = 0 
gcd = 1 



#Get user input and increment counter for male and female
numberEnrolles = int(input(f"number of enrolles: "))
for enrolees in range(1, numberEnrolles+1, 1) :
    inputGender = input(f"gender of person {enrolees}: ")
    if inputGender.lower() == "m":
        counterMale += 1
    elif inputGender.lower() == "f" :
        counterFemale +=1

print(f"Males: {counterMale}")
print(f"Females: {counterFemale}")

if numberEnrolles == counterMale :
    print("All males")
elif numberEnrolles == counterFemale :
    print("All females")
else :
# initilize GCD
    if counterFemale > counterMale :
        gcdinit = counterMale
    elif counterMale > counterFemale :
        gcdinit = counterFemale
    elif counterMale == counterFemale :
        gcdinit = counterFemale

#find gcd                
    for gcdcounter in range(gcdinit, 1, -1) :
        if (gcdcounter%counterFemale) != 0 :
            continue
        if (gcdcounter%counterMale) != 0 :
            continue
        gcd = gcdcounter
    print(f"{int(counterMale/gcd)}:{int(counterFemale/gcd)}")