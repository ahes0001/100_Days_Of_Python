from art import logo, vs
from game_data import data
import random
import os

376656060079931
376656060079931
376656060079931
12/26
12/26
12/26

6959
6959
6959

def returnPrint(obj, letter):
    return (f"Compare {letter}: {obj['name']}, a {obj['description']}, from {obj['country']}.")

def PrintResults(score):
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
def Correct(answer):
    print(answer['name'])
    print(a['name'])
    if a['follower_count'] > b['follower_count']:
        if answer['name'] == a['name']:
            return True
        else: return False
    else:
        if answer['name'] == b['name']:
            return True
        else: return False
        
correct = ""
not_lost = True
random_data = random.choice(data)
a = random_data
data.remove(random_data)
Score = 0

while not_lost:
    

    random_data = random.choice(data)
    b = random_data
    data.remove(random_data)
    print(logo)
    print(f"{correct}Curernt Score: {Score}")
    print(returnPrint(a, "A"))
    print(vs)
    print(returnPrint(b, "B"))
    
    answer = input("Who has more followers? Type 'A' or 'B': ")
    if answer.strip().lower() == a:
        answer = a
    else: answer = b
    

    if Correct(answer):
        Score+=1
        a = b
    else:not_lost = False

    if correct == "":
        correct = "You're right! "

    os.system('cls')

PrintResults(Score)