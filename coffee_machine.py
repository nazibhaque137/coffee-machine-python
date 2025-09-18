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
cash_register = 0

 # TODO 5: Process coins.
def payment(a):
    print("Please insert coins.")
    quarter= int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickels = int(input("How many nickels?"))
    pennies = int(input("How many pennies?"))
    amount_paid= (quarter* .25) + (dimes* .10) + (nickels * .05) + (pennies * .01)
    coffee_cost = MENU[a]["cost"]

 # TODO 6: Check transaction successful
    if amount_paid < coffee_cost:
        print("Please enter correct amount of coins. We have returned your coins.")
        return 0
    else:
        change = round(amount_paid - coffee_cost, 2)
        collected_money= coffee_cost
        if change == 0 :
            return collected_money
        else:
            print(f"Here is ${change} dollars in change")
            return  collected_money

# TODO 4 : Check resources sufficient
def resource_calculation(x):
    if x == "espresso" :
        if resources["water"] < MENU["espresso"]["ingredients"]["water"] :
            print("Sorry there is not enough water")
            return False
        elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"] :
            print("Sorry there is not enough coffee")
            return False
        else:
            return True
    elif x == "latte" :
        if resources["water"] < MENU["latte"]["ingredients"]["water"] :
            print("Sorry there is not enough water")
            return False
        elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"] :
            print("Sorry there is not enough coffee")
            return False
        elif resources["milk"] < MENU["latte"]["ingredients"]["milk"] :
            print("Sorry there is not enough milk")
            return False
        else:
            return True
    elif x == "cappuccino":
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
                print("Sorry there is not enough water")
                return False
        elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
                print("Sorry there is not enough coffee")
                return False
        elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
                print("Sorry there is not enough milk")
                return False
        else:
            return True

def make_coffee(x):
    for r in MENU[x]["ingredients"]:
        resources[r]=resources[r]-MENU[x]["ingredients"][r]

 # TODO 1: Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
order_Status = True

while order_Status is True :
    user_choiceOfCoffee = input("What would you like? (Espresso/Latte/Cappuccino) ").strip().lower()

 # TODO 2 : Turn off the Coffee Machine by entering “off” to the prompt.
    if user_choiceOfCoffee == "off" :
        order_Status = False

 #TODO 3 : Print report
    elif user_choiceOfCoffee == "report" :
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${cash_register}")


 # TODO 7: Make Coffee
    elif user_choiceOfCoffee in ("espresso" , "latte" , "cappuccino"):
        order_Status = resource_calculation(user_choiceOfCoffee)
        print(order_Status)
        if order_Status is False:
            break
        cash_status= cash_register
        cash_register += payment(user_choiceOfCoffee)
        if cash_status == cash_register :
            continue
        else:
            make_coffee(user_choiceOfCoffee)
            print(f"Here is your {user_choiceOfCoffee}. Enjoy!")

    else:
        print("Invalid choice. Please try again.")





