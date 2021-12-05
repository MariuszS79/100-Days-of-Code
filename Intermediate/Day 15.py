import os

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

coffee = "☕"


def off():
    if what_coffee == "off":
        os._exit(100)


def report():
    if what_coffee == "report":
        for key, value in resources.items():
            print(key, ':', value)
        print(f"Money : ${profit}")


def check_ingeredients():
    if what_coffee in MENU:
        print(f'{what_coffee}', MENU[what_coffee]['ingredients'])
        if MENU[what_coffee]['ingredients']["water"] > resources["water"]:
            print("Sorry there is not enough water.")
        if "milk" in "ingredients" and MENU[what_coffee]['ingredients']["milk"] > resources["milk"]:
            print("Sorry there is not enough milk.")
        if MENU[what_coffee]['ingredients']["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee.")


what_coffee = input("What coffee would you like? (espresso/latte/cappuccino): ")
off()
report()
check_ingeredients()
