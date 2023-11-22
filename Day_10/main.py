from art import logo

def calculate(x,y,symbol):
    """
    assume x and y are integers or floats while symbol is a string.
    the operation will excute relative to given order
    """
    if symbol == "+":
        return x+y
    if symbol == "-":
        return x-y
    if symbol == "*":
        return x*y
    if symbol == "/":
        return x/y
    
print(logo)
loop = True

userInputFirstNumber = input("What is the first number?: ")
userInputOperation = ''
userInputNextNumber = 0
while loop:
    print("\n+\n-\n*\n/")
    userInputOperation = input("Pick an operation: ")
    userInputNextNumber = input("What is the next number?: ")
    print("userInputFirstNumber:",userInputFirstNumber,"userInputNextNumber: ",userInputNextNumber)
    output = calculate(float(userInputFirstNumber),float(userInputNextNumber),userInputOperation)
    print(f"{userInputFirstNumber} {userInputOperation} {userInputNextNumber} = {output}")

    nextCalculation = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calcualtion else 'e' to exit: ")
    if nextCalculation.lower() == 'y':
        userInputFirstNumber = output
    elif nextCalculation.lower() == 'n':
        userInputFirstNumber = input("What is the first number?: ")
    elif nextCalculation.lower() == 'e':
        loop = False
# else print("invalid input")



    
