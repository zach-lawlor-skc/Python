import random
number = random.randint (1,10)
print (number)

count = 0
while count < 3 :
     guess = int(input("Enter a number between 1 and 10: "))
     if guess == number:
         print("Correct")
         break
     elif guess < number:
        print("Too low")
     else:
        print ("Too high")
        
     count = count + 1
    
print("see you again")
    