ageShem = int(input("enter age: "))
priceWashingMachine = float(input("price of washing machine: "))
priceOfToySold = float(input("price of Toy Sold: "))
numberOfToys = 0
moneyInPiggyBank = 0
dollarIncrement = 0

for i in range(1,ageShem+1,1) :
    if i%2 == 0 :
        dollarIncrement += 10
        moneyInPiggyBank += dollarIncrement ## money
        moneyInPiggyBank -= 1 ## stolen
    else :
        numberOfToys += 1
totalMoney = moneyInPiggyBank + numberOfToys*priceOfToySold

if totalMoney >= priceWashingMachine :
    print(f"Yes! you still have {(totalMoney - priceWashingMachine) :.2f} left")
else :
    print(f"No! you still need {(priceWashingMachine - totalMoney) :.2f}")
    