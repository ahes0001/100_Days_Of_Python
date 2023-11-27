MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def possible(drink):
    if resources["water"] >= MENU[drink]['ingredients']['water'] and resources["coffee"] >= MENU[drink]['ingredients']['coffee']:
        if drink == "espresso":
            return True
        elif resources["milk"] >= MENU[drink]['ingredients']['milk']:
            return True
        else:
            return False

    else:
        return False


def sorry_message(drink):
    insufficient = ""
    if resources["water"] <= MENU[drink]['ingredients']['water']:
        insufficient += "water"
    if resources["coffee"] <= MENU[drink]['ingredients']['coffee']:
        if insufficient == "":
            insufficient += "coffee"
        else:
            insufficient += ", coffee"
    if drink != "espresso":
        if resources["milk"] <= MENU[drink]['ingredients']['milk']:
            if insufficient == "":
                insufficient += "milk"
            else:
                insufficient += ", milk"
    return f"Sorry there is not enough {insufficient}."


def purchase_results(drink, num_of_quarters, num_of_dimes, num_of_nickles, num_of_pennies):
    total_money = 0.25*num_of_quarters + 0.10*num_of_dimes + 0.5*num_of_nickles + 0.01*num_of_pennies
    if MENU[drink]['cost'] > total_money:
        return "Insufficient funds money returned"
    else:
        print(f"Here is {str(round(total_money-MENU[drink]['cost'],2))} in change.")
        print(f"Here is your {drink}. Enjoy!")
        resources['money'] += MENU[drink]['cost']
        resources['water'] -= MENU[drink]['ingredients']['water']
        if drink != "espresso":
            resources['milk'] -= MENU[drink]['ingredients']['milk']
        resources['coffee'] -= MENU[drink]['ingredients']['coffee']
    # assuming drink is possible to make
    #case 1: fail --> not enough money, money refunded
    #case 2: sucesed --> calcualte change + give coffee


def print_report():
    print("Water:", str(resources['water']) + "ml")
    print("Milk:", str(resources['milk']) + "ml")
    print("Coffee:", str(resources['coffee']) + "g")
    print("Money:", "$" + str(resources['money']))


running = True
while running:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    user_input = user_input.strip().lower()
    if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        if possible(user_input):
            print("Please insert coins.")
            num_of_quarters = int(input("How many quarters?"))
            num_of_dimes = int(input("How many dimes?"))
            num_of_nickles = int(input("How many nickles?"))
            num_of_pennies = int(input("How many pennies?"))
            purchase_results(user_input, num_of_quarters, num_of_dimes, num_of_nickles, num_of_pennies)
        else:
            print(sorry_message(user_input))
    elif user_input == "report":
        print_report()
    elif user_input == "end":
        running = False
    else:
        print("Input unrecognized. Please try again.")


