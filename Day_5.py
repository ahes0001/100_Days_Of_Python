#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

output = ""

print("Welcome to the PyPassword Generator!")
numOfLetters = input("How many letters would you like in your password?")
numOfSymbols = input("How many Symbols would you like?")
numOfNumbers = input("How many Numbers would you like?")

try:
    numOfLetters= int(numOfLetters.strip())
    numOfNumbers = int(numOfNumbers.strip())
    numOfSymbols = int(numOfSymbols.strip())
except:
    print("Invalid input!")
else:
    addedLetters = 0
    addedSymbols = 0
    addedNumbers = 0

    while len(output) <numOfLetters+numOfSymbols+numOfNumbers:
        randLetter = random.randint(0,51)
        randInt = random.randint(0,9)
        randSymbol = random.randint(0,8)
        do = random.randint(0,2)
        if do == 0 and addedLetters<numOfLetters:
            output+=letters[randLetter]
            addedLetters+=1
        elif do == 1 and addedNumbers<numOfNumbers:
            output+=numbers[randInt]
            addedNumbers+=1
        elif do == 2 and addedSymbols<numOfSymbols:
            output+=symbols[randSymbol]
            addedSymbols+=1

    print("Here is your password:", output)