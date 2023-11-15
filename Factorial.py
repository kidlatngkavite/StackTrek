## initialization 0! and 1! equals 1. Start loop at 2
factorial = 1
numberInput = int(input("enter number: "))


#loop starts at 2, increments by one then multiplies the previos number with the current number
for iteration in range(2,numberInput+1,1) :
    factorial *= iteration

# print factorial
print(f"{factorial}")
