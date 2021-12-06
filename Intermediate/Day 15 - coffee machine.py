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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


cash_in_machine = 0
quarters = 0
dimes = 0
nickles = 0
pennies = 0
no_ingredient = False


def off():
    global machine_is_on
    if what_coffee == "off":
        machine_is_on = False


def report():
    if what_coffee == "report":
        for key, value in resources.items():
            print(key, ':', value)
        print(f"Money : ${profit}")


def check_ingeredients():
    global no_ingredient
    if what_coffee in MENU:
        if MENU[what_coffee]['ingredients']["water"] > resources["water"]:
            print("Sorry there is not enough water.")
            no_ingredient = True
        if "milk" in "ingredients" and MENU[what_coffee]['ingredients']["milk"] > resources["milk"]:
            print("Sorry there is not enough milk.")
            no_ingredient = True
        if MENU[what_coffee]['ingredients']["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee.")
            no_ingredient = True


def insert_coins():
    global quarters
    global dimes
    global nickles
    global pennies
    global cash_in_machine
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    cash_in_machine = cash_in_machine+(quarters*0.25)
    dimes = int(input("How many dimes?: "))
    cash_in_machine = cash_in_machine + (dimes * 0.1)
    nickles = int(input("How many nickles?: "))
    cash_in_machine = cash_in_machine + (nickles * 0.05)
    pennies = int(input("How many pennies?: "))
    cash_in_machine = cash_in_machine + (pennies * 0.01)


def is_transaction_succesful():
    global cash_in_machine
    global profit
    if MENU[what_coffee]['cost'] > cash_in_machine:
        print("Sorry that's not enough money. Money refunded.")
        cash_in_machine = 0
    else:
        resources["water"] = resources["water"] - MENU[what_coffee]['ingredients']["water"]
        resources["coffee"] = resources["coffee"] - MENU[what_coffee]['ingredients']["coffee"]
        if "milk" in MENU[what_coffee]['ingredients']:
            resources["milk"] = resources["milk"] - MENU[what_coffee]['ingredients']["milk"]
        if cash_in_machine > MENU[what_coffee]['cost']:
            rest = round(cash_in_machine - MENU[what_coffee]['cost'], 2)
            print(f"Here is ${rest} in change")
            cash_in_machine = 0
            profit = round(profit + MENU[what_coffee]['cost'], 2)
        print(f"Here is your {what_coffee} ☕. Enjoy!")


def topup():
    global resources
    global no_ingredient
    if what_coffee == "topup":
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100
        no_ingredient = False
        print("The machine has been filled")


machine_is_on = True

while machine_is_on:

    what_coffee = input("What coffee would you like? (espresso/latte/cappuccino): ")
    topup()
    if what_coffee == "topup":
        continue
    off()
    if machine_is_on is False:
        break
    report()
    if what_coffee == "report":
        continue
    check_ingeredients()
    if no_ingredient is True:
        continue
    insert_coins()
    is_transaction_succesful()
