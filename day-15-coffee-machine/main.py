
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
}

profit = 0
choice = True
#TODO - 2 Functions

def resource_check(drink_name):
    if drink_name == 'espresso':
        if resources["water"] >= MENU[drink_name]["ingredients"]["water"] and resources["coffee"] >= MENU[drink_name]["ingredients"]["coffee"]:
            return True
        else:
            return False
    elif drink_name == 'latte':
        if resources["water"] >= MENU[drink_name]["ingredients"]["water"] and resources["milk"] >= MENU[drink_name]["ingredients"]["milk"] and resources["coffee"] >= MENU[drink_name]["ingredients"]["coffee"]:
            return True
        else:
            return False
    else:
        if resources["water"] >= MENU[drink_name]["ingredients"]["water"] and resources["milk"] >= MENU[drink_name]["ingredients"]["milk"] and resources["coffee"] >= MENU[drink_name]["ingredients"]["coffee"]:
            return True
        else:
            return False

def make_coffee(drink_name):
    if drink_name == 'espresso':
        resources["water"] -= MENU[drink_name]["ingredients"]["water"]
        resources["coffee"] -= MENU[drink_name]["ingredients"]["coffee"]
    else:
        resources["water"] -= MENU[drink_name]["ingredients"]["water"]
        resources["milk"] -= MENU[drink_name]["ingredients"]["milk"]
        resources["coffee"] -= MENU[drink_name]["ingredients"]["coffee"]
    print(f"Here is your {drink_name}")

#TODO - 1 Main Loop / Operation
while choice:
    flavour = input("What would you like? Espresso, Latte, Cappuccino, Report, Turn Off ").lower()
    if flavour == 'report':
        x = resources["water"]
        y = resources["milk"]
        z = resources["coffee"]
        print(f"Water {x}")
        print(f"Milk {y}")
        print(f"coffee {z}")
        print(f"Profit is: ${profit}")
    elif flavour == 'turn off':
        break
    else:
        if resource_check(flavour):
            print("Insert Coins")
            penny = int(input("Penny?"))
            nickel = int(input("Nickels"))
            dimes = int(input("Dimes?"))
            quarters = int(input("Quarters"))
            total = (penny * 0.01) + (nickel * 0.05) + (dimes * 0.10) + (quarters * 0.25)
            if flavour == 'cappuccino':
                total_cost = 3
                if total >= total_cost:
                    change_from_coins = total - total_cost
                    f = round(change_from_coins,2)
                    print(f"Your change is {f}")
                    make_coffee(flavour)
                    profit += total_cost
                else:
                    print("Not enough coins")
            elif flavour == 'latte':
                total_cost = 2.5
                if total >= total_cost:
                    change_from_coins = total - total_cost
                    g = round(change_from_coins,2)
                    print(f"Your change is {g}")
                    make_coffee(flavour)
                    profit += total_cost
                else:
                    print("Not enough coins")
            else:
                total_cost = 1.5
                if total >= total_cost:
                    change_from_coins = total - total_cost
                    h = round(change_from_coins, 2)
                    print(f"Your change is {h}")
                    make_coffee(flavour)
                    profit += total_cost
                else:
                    print("Not enough coins")
