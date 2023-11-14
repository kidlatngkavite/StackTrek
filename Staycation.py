month = input("Month: ")
days = int(input("Days of Stay: "))
discountDeLuxe = 0


if days > 14 :
    discountPremium = 0.10
else :
    discountPremium = 0

if month == "May" or month == "October":
    costDeLuxe = 100.00
    costPremium = 85.00
    if days > 7 and days <= 14 :
        discountDeLuxe = 0.05
    elif days > 14 :
        discountDeLuxe = 0.30

elif month == "July" or month == "September":
    costDeLuxe = 112.50
    costPremium = 90.58
    if days > 14 :
        discountDeLuxe = 0.20
elif month == "June" or month == "August":
    costDeLuxe = 125.66
    costPremium = 100.50



print(f"Deluxe: {(costDeLuxe*days*(1 - discountDeLuxe)):.2f} dollars")
print(f"Premium: {(costPremium*days*(1 - discountPremium)):.2f} dollars")