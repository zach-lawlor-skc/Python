import random

number = random.randint(1,10)

guess = int(input("Enter a number between 1 and 10: "))
if guess == number:
    print("Your guess was correct. Well done!")
    print ("See you again.")
else:
    if guess != number:
        print ("Hard luck. Your guess was wrong.")
        
