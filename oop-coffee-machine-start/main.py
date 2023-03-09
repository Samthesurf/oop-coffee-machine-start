from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# Get the MenuItem objects for each coffee choice from the menu
espresso = menu.find_drink("espresso")
latte = menu.find_drink("latte")
cappuccino = menu.find_drink("cappuccino")

while True:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_choice == 'report':
        coffee_maker.report()
        money_machine.report()
        continue  # it restarts the loop after giving the report
    if coffee_choice == 'espresso':
        drink = espresso
    elif coffee_choice == "latte":
        drink = latte
    elif coffee_choice == "cappuccino":
        drink = cappuccino
    elif coffee_choice == 'off':
        break
    if not coffee_maker.is_resource_sufficient(drink):
        break
    if money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)  # make the coffee
    else:
        break
