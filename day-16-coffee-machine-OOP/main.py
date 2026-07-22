from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

options = menu.get_items()

turn_on = True

while turn_on:
    choice = input(f"What would you like to have {options}report/off").lower()
    if choice == 'off':
        turn_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        item = menu.find_drink(choice)
        aval = coffee_maker.is_resource_sufficient(item)
        total_cost = money_machine.make_payment(item.cost)
        if aval and total_cost:
            coffee_maker.make_coffee(item)
