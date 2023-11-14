numberArray = []
numberInput = 0
countDivby3 = 0
numberMax = 0
numberMin = 0


for i in range(10):
    numberInput = int(input("enter number: "))
    if i == 0 :
        numberMax = numberInput
        numberMin = numberInput
        if (numberInput%3) == 0 :
            countDivby3 += 1
    else:
        if numberInput > numberMax :
            numberMax = numberInput
        if numberInput < numberMin :
            numberMin = numberInput
        if (numberInput%3) == 0 :
            countDivby3 += 1

print(f"Highest: {numberMax}")
print(f"Lowest: {numberMin}")
print(f"{countDivby3} numbers divisible by 3")