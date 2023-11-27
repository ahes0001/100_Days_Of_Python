from art import logo, vs
from game_data import data
import random
import os


def return_print(obj, letter):
    return f"Compare {letter}: {obj['name']}, a {obj['description']}, from {obj['country']}."


def print_results(score):
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")


def correct(answer):
    print(answer['name'])
    print(a['name'])
    if a['follower_count'] > b['follower_count']:
        if answer['name'] == a['name']:
            return True
        else:
            return False
    else:
        if answer['name'] == b['name']:
            return True
        else:
            return False


one_correct = ""
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
    print(f"{one_correct}Current Score: {Score}")
    print(return_print(a, "A"))
    print(vs)
    print(return_print(b, "B"))
    
    answer = input("Who has more followers? Type 'A' or 'B': ")
    if answer.strip().lower() == a:
        answer = a
    else:
        answer = b

    if correct(answer):
        Score += 1
        a = b
    else:
        not_lost = False

    if one_correct == "":
        one_correct = "You're right! "

    os.system('cls')

print_results(Score)
