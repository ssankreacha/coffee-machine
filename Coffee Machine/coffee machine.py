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
coffee_machine_on = True
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def begin_coffee_machine():
    global choice
    choice = input("what would you like (espresso/latte/cappuccino)? ").lower()
    if choice == "report":
        print(f"Water: {resources["water"]}ml  \nMilk: {resources["milk"]}ml  \nCoffee: {resources["coffee"]}g")
        print(f"Money: {profit}")
        begin_coffee_machine()
    elif choice == "off":
        exit()          # Alternatively, coffee_machine_on = False


begin_coffee_machine()


def cost():
    global quarters
    quarters = int(input("Please insert Coins. \nHow many Quarters: ")) * 0.25
    global dimes
    dimes = int(input("How many Dimes?: ")) * 0.10
    global nickles
    nickles = int(input("How many Nickles: ")) * 0.05
    global pennies
    pennies = int(input("How many Pennies: ")) * 0.01


while coffee_machine_on:
    if choice == "espresso":
        if choice == "espresso" and resources["water"] < 50:
            print("Sorry, not enough water. ")
            begin_coffee_machine()
        elif choice == "espresso" and resources["coffee"] < 18:
            print("Sorry, not enough coffee. ")
            begin_coffee_machine()
        else:
            cost()
            espresso_cost = MENU["espresso"]["cost"]
            espresso_payment = quarters + dimes + nickles + pennies
            if espresso_payment < espresso_cost:
                print("Sorry, that is not enough 😫 Money refunded. ")
                begin_coffee_machine()
            else:
                espresso_change = round(espresso_payment - espresso_cost, 2)
                print(f"Enjoy your Espresso ☕! Here is your change ${espresso_change}. Next please. ")
                profit += espresso_cost
                resources["water"] -= int(50)
                resources["coffee"] -= int(18)
                begin_coffee_machine()

    elif choice == "cappuccino":
        if choice == "cappuccino" and resources["water"] < 250:
            print("Sorry, not enough water. ")
            begin_coffee_machine()
        elif choice == "cappuccino" and resources["milk"] < 100:
            print("Sorry, not enough milk. ")
            begin_coffee_machine()
        elif choice == "cappuccino" and resources["coffee"] < 24:
            print("Sorry, not enough coffee. ")
            begin_coffee_machine()
        else:
            cost()
            cappuccino_cost = MENU["cappuccino"]["cost"]
            cappuccino_payment = quarters + dimes + nickles + pennies
            if cappuccino_payment < cappuccino_cost:
                print("Sorry that is not enough 😫 Money refunded. ")
                begin_coffee_machine()
            else:
                cappuccino_change = round(cappuccino_payment - cappuccino_cost, 2)
                print(f"Enjoy your Cappuccino ☕! Here is your change ${cappuccino_change}. Next please. ")
                profit += cappuccino_cost
                resources["water"] -= int(250)
                resources["milk"] -= int(100)
                resources["coffee"] -= int(24)
                begin_coffee_machine()

    elif choice == "latte":
        if choice == "latte" and resources["water"] < 200:
            print("Sorry, not enough water. ")
            begin_coffee_machine()
        elif choice == "latte" and resources["milk"] < 150:
            print("Sorry, not enough milk. ")
            begin_coffee_machine()
        elif choice == "latte" and resources["coffee"] < 24:
            print("Sorry, not enough coffee. ")
            begin_coffee_machine()
        else:
            cost()
            latte_cost = MENU["latte"]["cost"]
            latte_payment = quarters + dimes + nickles + pennies
            if latte_payment < latte_cost:
                print("Sorry that is not enough 😫 Money refunded. ")
                begin_coffee_machine()
            else:
                latte_change = round(latte_payment - latte_cost, 2)
                print(f"Enjoy your Latte ☕! Here is your change ${latte_change}. Next please. ")
                profit += latte_cost
                resources["water"] -= int(200)
                resources["milk"] -= int(150)
                resources["coffee"] -= int(24)
                begin_coffee_machine()
