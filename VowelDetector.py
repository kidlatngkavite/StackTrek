
count = 0

inputString = input("input string: ")
               
           

if "a" in inputString.lower() :
    count = count + 1 
    vowel = "a"
if "e" in inputString.lower() :
    count = count + 1 
    vowel = "e"
if "i" in inputString.lower() :
    count = count + 1 
    vowel = "i"
if "o" in inputString.lower() :
    count = count + 1 
    vowel = "o"
if "u" in inputString.lower() :
    count = count + 1 
    vowel = "u"

if count > 1 :
    print(f"There are {count} different vowels in the string.")
elif count == 1:
    print("There is only one different vowel in the string.")
elif count == 0 :
    print("There are no vowels in the string.")