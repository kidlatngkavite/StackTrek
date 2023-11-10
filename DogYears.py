EQUIVALENTFIRST2YEARS = 10.5
EQUIVALENTSUCCEEDINGYEARS = 4

years = int(input("Years: "))

if years <= 2 :
    print(f"{years*EQUIVALENTFIRST2YEARS}")
else :
    print(f"{21 + ((years-2)*EQUIVALENTSUCCEEDINGYEARS)}") #question


    
