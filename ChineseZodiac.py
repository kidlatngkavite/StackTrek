year = int(input("Year: "))

if year < 0 :
    print("Invalid Year")
elif (year%12) == 0:
    print("Monkey")
elif (year%12) == 1:
    print("Rooster")
elif (year%12) == 2:
    print("Dog")
elif (year%12) == 3:
    print("Boar")
elif (year%12) == 4:
    print("Rat")    
elif (year%12) == 5:
    print("Ox")
elif (year%12) == 6:
    print("Tiger")
elif (year%12) == 7:
    print("Hare")
elif (year%12) == 8:
    print("Dragon")
elif (year%12) == 9:
    print("Snake")
elif (year%12) == 10:
    print("Horse")
elif (year%12) == 11:
    print("Sheep")
