ageInput = 0
guestCounter = 0
costOfGroup = 0
admisstionCostBabies = 0.00
admisstionCostChildren = 14.00
admisstionCostSeniors = 18.00
admisstionCostOthers = 23.00

while True:
    guestCounter  += 1
    ageInput = input(f"inpute age of guest {guestCounter}: ")
    if ageInput == "end" :
        break
    if int(ageInput) <= 2 :
        costOfGroup += admisstionCostBabies
    elif int(ageInput) >= 3 and int(ageInput) <= 12 :
        costOfGroup += admisstionCostChildren
    elif int(ageInput) >= 65 :
        costOfGroup += admisstionCostSeniors
    else :
        costOfGroup += admisstionCostOthers

print(f"{costOfGroup:.2f}")