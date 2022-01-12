import random
number =random.randint(1,2)




guess = int(input("Is the number 1 or 2: "))
if guess == number:
    print("Right")
else:
    print("Wrong")
            