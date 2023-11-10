COSTOFPUZZLE = 14.00
COSTOFTALKINGDOLL = 3.00
COSTOFTEDDYBEAR = 20.20
COSTOFPOKEMONPLUSHIE = 8.20
COSTOFBIGTOYTRUCK = 10.65

targetDonation = float(input("Target Donation: "))
numberOfPuzzles = float(input("Number of Puzzles: "))
numberOfTalkingDolls = float(input("Number of Talking Dolls: "))
numberOfTeddyBears = float(input("Number of Teddy Bears "))
numberOfPokemonPlushies = float(input("Number of Pokémon Plushies: "))
numberOfBigToyTrucks = float(input("Number of Big Toy Trucks: "))


totalCostOfPuzzles = numberOfPuzzles * COSTOFPUZZLE
totalCostOfTalkingDolls = numberOfTalkingDolls * COSTOFTALKINGDOLL
totalCostOfTeddyBears = numberOfTeddyBears * COSTOFTEDDYBEAR
totalCostOfPokemonPlushies = numberOfPokemonPlushies * COSTOFPOKEMONPLUSHIE
totalCostOfBigToyTrucks = numberOfBigToyTrucks * COSTOFBIGTOYTRUCK
totalNumberofOrder = numberOfPuzzles + numberOfTalkingDolls + numberOfTeddyBears + numberOfPokemonPlushies + numberOfBigToyTrucks

if totalNumberofOrder >= 50 :
    totalCostofOrder = 0.75*(totalCostOfPuzzles + totalCostOfTalkingDolls + totalCostOfTeddyBears + totalCostOfPokemonPlushies + totalCostOfBigToyTrucks)
else :
    totalCostofOrder = totalCostOfPuzzles + totalCostOfTalkingDolls + totalCostOfTeddyBears + totalCostOfPokemonPlushies + totalCostOfBigToyTrucks

leftAfterRental = 0.9*totalCostofOrder
if (leftAfterRental - targetDonation ) > 0 :
    print(f"Yes! {(leftAfterRental - targetDonation):.2f} dollars left.") #question on formating inside parenthesis
else :
    print(f"Not enough money! {(targetDonation - leftAfterRental):.2f} dollars needed.")