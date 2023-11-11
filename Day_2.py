print("Welcome to the tip calculator!")
totalBill = float(input("What was the total bill? $"))
numOfPeople = int(input("How many people to split the bill?(Whole number)\n"))
percentTip = int(input("What percent tip would you like to give?(Whole number)\n"))
billPerPerson = totalBill*(1+percentTip/100)/numOfPeople
print(f"Each person should pay: {billPerPerson: .2f}")



