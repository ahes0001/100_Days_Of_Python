import os
from art import logo
#purpose create silient biding platform
#from one device
#NOTICE THERE IS NO VALIDATION

biddersDict = {}
print(logo)
print("Welcome to the secret auction program.")
nextBidder = True

while nextBidder:
    name = input("What is you name?: ")
    bid = int(input("What is your bid? $"))
    #add key value pair
    biddersDict[name] = bid

    otherBidders = input("Are there any other bidders? Type 'yes' or 'no'.")
    if otherBidders.strip().lower() == "no":
        nextBidder = False
    else: os.system('cls')

#find winner
max_key = max(biddersDict, key=biddersDict.get)  # Finds the key with the maximum value
max_value = biddersDict[max_key]

print("The winner is",max_key, "with a bid of $"+ str(max_value))

