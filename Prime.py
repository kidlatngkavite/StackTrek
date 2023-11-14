numberInput = int(input("enter number: "))
if numberInput <= 1 :
        isPrime = False
else :
    isPrime = True


for i in range(2,numberInput,1) :

    primeCheck =  numberInput % i
    if primeCheck == 0 :    
        isPrime = False
        break
    

if isPrime:
    print("Prime")
else :
    print("Not Prime")
