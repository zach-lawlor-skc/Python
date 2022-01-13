import random
counties = ["Carlow", "Dublin", "Kildare", "Kilkenny", "Laois", "Longford", "Louth", "Meath", "Offaly", "Westmeath", "Wexford", "Wicklow",  "Clare", "Cork", "Kerry", "Limerick", "Tipperary", "Waterford", "Antrim", "Armagh", "Cavan", "Donegal", "Down", "Fermanagh", "Derry", "Monaghan", "Tyrone","Galway", "Leitrim", "Mayo", "Roscommon","Sligo"]
random.shuffle(counties)
count = 0
county = counties[0:1]
print(county)

while count <=10:
    guess = input("What county am I thinking of? ")
    if guess == county:
        print("Well done")
        break
    elif guess != county:
        print("Try again")
        
    count=count + 1

if count > 10:
    print("Sorry, you are out of luck. The answer was:",county)
        
       
        
print("Goodbye")        
        
        
    

