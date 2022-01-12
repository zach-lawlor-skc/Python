import random
eu = ["Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia", "Spain", "Sweden"]
random.shuffle(eu)
ans=print(eu [0:1])
ans=(eu [0:1])
guess=input("What country am I thinking of: ")
guess.title()
if guess == ans:
    print("Well done, you're a genius!")
while guess != ans:
    again= input("Have another go: ")
    