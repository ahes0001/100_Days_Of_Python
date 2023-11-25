from art import logo
import random
############### Blackjack Project #####################

#Difficulty Normal 😎:Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is as expected 52 cards and 4 suits.  
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are removed from the deck as they are drawn.
## The computer is the dealer.


playerHand = []
computerHand = []

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deck = [(value, suit) for suit in suits for value in values]



def presentTable():
    plural = ""
    print(f"You have {len(playerHand)} cards:")
    for card in playerHand:
        print(card[0]+" of " +card[1])
    print(f"Computer has {len(computerHand)} cards:")
    print(computerHand[0][0]+" of " +computerHand[0][1])
    if len(computerHand) >2:
        plural = "s"
    print(f"{len(computerHand)-1} unrevealed card{plural}")
    print('')



#hand out cards 2 each
# if comp <16 take another card if >21 comp loses
#present table

#give player decide if he wants second card for fold if >21 comp loses 
#ELSE fold
#when fold check results

def card_value(card):
    value = card[0]
    if value in ['J', 'Q', 'K']:
        return 10
    elif value == 'A':
        return 11  # Initially consider Ace as 11
    else:
        return int(value)

def dealCards():

    for _ in range(2):
        random_card = random.choice(deck)
        playerHand.append(random_card)
        deck.remove(random_card)

        random_card = random.choice(deck)
        computerHand.append(random_card)
        deck.remove(random_card)

    total_value = sum(card_value(card) for card in computerHand)
    while total_value <16:
        print("dealer decided to hit!")
        random_card = random.choice(deck)
        computerHand.append(random_card)
        deck.remove(random_card)
        total_value = sum(card_value(card) for card in computerHand)
    print("dealer decided to stand!")

def checkForLoser(hand, who):
    total_value = sum(card_value(card) for card in hand)
    if total_value>21:
        print(f"{who} has lost by exceeding 21! Busted!")
        return False
    return True

def Results():
    total_value_computer = sum(card_value(card) for card in computerHand)
    total_value_player = sum(card_value(card) for card in playerHand)
    if (total_value_computer > total_value_player and total_value_computer <22) or total_value_player > 21:
        return "You have lost!"
    elif (total_value_player > total_value_computer or total_value_player <22) or total_value_computer > 21:
        return "You have won!"
    else: return f"DRAW of {total_value_computer} points!!!"
    
noOneLost = True
notFolded = True
print(logo)
dealCards() #and computer choses to stake or not
presentTable()
noOneLost = checkForLoser(computerHand, "Dealer")
while noOneLost and notFolded:
    stake = input("Would you like to hit or stand?(input 'h' or 's'): ") 
    if stake == 'h':
        random_card = random.choice(deck)
        playerHand.append(random_card)
        deck.remove(random_card)
        presentTable()
        noOneLost = checkForLoser(playerHand, "You")
    elif stake == 's':
        notFolded = False

print(Results())
print("")

print(f"Dealer had {len(computerHand)} cards:")
for card in computerHand:
    print(card[0]+" of " +card[1])
total_value_computer = sum(card_value(card) for card in computerHand)
print(f"With a total of {total_value_computer} points.")








# for _ in range(10):
#     random_card = random.choice(deck)
#     print(random_card)
#     deck.remove(random_card)

#     random_card = random.choice(deck)
#     print(random_card)
#     deck.remove(random_card)

