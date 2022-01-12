import random

name = input("Hello, what is your name? ")
print("Welcome",name)

number = random.randint(1,10)
#print(number)

guess = int(input("Take a guess between 1 and 10, best of luck!: "))

if guess == number:
    print("Your guess was correct!")
    print("Well done!")
   
elif guess != number:
    print("Hard luck, your guess was incorrect.")
    
if guess < number:
    print("Too low!")
   
else:
    print("Too high!")
