day = int(input("Day: "))
month = input("Month: ")



if month == "january":
    if day >= 1 and day <= 19 :
        sign = "Capricorn"
    else:
         sign = "Aquarius"
elif month == "february":
    if day >= 1 and day <= 18 :
        sign = "Aquarius"
    else:
         sign = "Pisces"
elif month == "march":
    if day >= 1 and day <= 20 :
        sign = "Pisces"
    else:
         sign = "Ares"         
elif month == "april":
    if day >= 1 and day <= 19 :
        sign = "Aries"
    else:
         sign = "Taurus"      
elif month == "may":
    if day >= 1 and day <= 20 :
        sign = "Taurus"
    else:
         sign = "Gemini"     
elif month == "june":
    if day >= 1 and day <= 20 :
        sign = "Gemini"
    else:
         sign = "Cancer"     
elif month == "july":
    if day >= 1 and day <= 22 :
        sign = "Cancer"
    else:
         sign = "Leo"     
elif month == "august":
    if day >= 1 and day <= 22 :
        sign = "Leo"
    else:
         sign = "Virgo"     
elif month == "september":
    if day >= 1 and day <= 22 :
        sign = "Virgo"
    else:
         sign = "Libra"  
elif month == "october":
    if day >= 1 and day <= 22 :
        sign = "Libra"
    else:
         sign = "Scorpio"  
elif month == "november":
    if day >= 1 and day <= 21 :
        sign = "Scorpio"
    else:
         sign = "Sagittarius"  
elif month == "december":
    if day >= 1 and day <= 21 :
        sign = "Sagittarius"
    else:
         sign = "Capricorn"  

print(f"Your Astrological sign is : {sign}")