from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffe_maker_01 = CoffeeMaker()
menu_01 = Menu()
money_machine_01 = MoneyMachine()

running = True
while running:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    user_input = user_input.strip().lower()
    if menu_01.find_drink(user_input) is not None:
        if coffe_maker_01.is_resource_sufficient(menu_01.find_drink(user_input)):
            if money_machine_01.make_payment(menu_01.find_drink(user_input).cost): #if payment is made
                coffe_maker_01.make_coffee(menu_01.find_drink(user_input))
    elif user_input == "report":
        coffe_maker_01.report()
    elif user_input == "end":
        running = False