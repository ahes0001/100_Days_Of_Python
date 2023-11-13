import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
def printRPS(hand):
    if hand == 0:
        return(rock)
    elif hand == 1:
        return(paper)
    elif hand == 2:
        return(scissors)
    else: return("Invalid Input!")


inputU = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
try:
    inputU = int(inputU)
except:
    print("Invalid Input!")

print("You chose:\n",printRPS(inputU))
randInt = random.randint(0,2)
print("\nComputer chose:\n",printRPS(randInt))


if inputU == randInt:
    print("DRAW!")
    #  0 - rock 1 - paper 2- scissors
elif inputU == 0 and randInt == 2:
    print("YOU WIN!")
elif inputU == 1 and randInt == 0:
    print("YOU WIN!")
elif inputU == 2 and randInt == 1:
    print("YOU WIN!")
else:
    print("YOU LOSE!")







