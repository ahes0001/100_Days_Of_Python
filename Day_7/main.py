import random
from hangman_art import stages, logo
from hangman_words import word_list

#Purpose: implementation of hangman
#WARNING THE GAME HAS NO INPUT VALIDATION

print(logo)
# generate random word

# LOOP: WHILE BLANKS ARE ALL NOT UNCOVERED
# ask for input, reveal blanks
# show hangman progression


hangmanState = 0
chosen_word = random.choice(word_list)
revealed = []
lettersRevealed = 0
for i in range(len(chosen_word)):
    revealed.append("_")


def ReturnRevealedWord():
    output= ''
    for letter in range(len(revealed)):
        output += revealed[letter]+" "
    return(output)

def ReturnHangmanState():
    return stages[hangmanState]

while hangmanState>len(stages)*-1 and lettersRevealed<len(chosen_word):
    letterGuessed = input("Guess a letter: ")
    # validate letter in word
    # return feed back either correct or incorrect
    #DONE: print revealed word
    #DONE: print hang man
    if (letterGuessed in chosen_word):
        for i in range(len(chosen_word)):
            if letterGuessed in chosen_word[i]:
                revealed[i] = letterGuessed
                lettersRevealed +=1
        
        print(ReturnRevealedWord())
        print(ReturnHangmanState())
    else:
        print(ReturnRevealedWord())
        print(f"You guessed {letterGuessed}, that's no tin the word. You lose a life!")
        hangmanState -=1
        print(ReturnHangmanState())

if not(lettersRevealed<len(chosen_word)):
    print("You win!")
else:
    print("You lost!")
    