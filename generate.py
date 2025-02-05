#modules 
#random module ( to generate random number/choice and help shuffle a list)

import random 

#use from to import a particular module into a variable
#from random import choice
#coin = choice(["heads","tails"])

#provide a random choice
coin = random.choice(["heads","tails"])
print(coin)

#generate a random num between a range
number = random.randint(1,10)
print(number)

#shuffle a list
cards = ["jack","queen","king"]
random.shuffle(cards)
for card in cards:
    print(card)
