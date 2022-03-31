menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}
run = True


def checkResources(drink, resource):
    wantedDrink = menu[drink]["ingredients"]
    ingrlist = ["water", "milk", "coffee"]
    for i in ingrlist:
        if wantedDrink[i] > resource[i]:
            print(f"Sorry, there is not enough {i}")
            exit()
    else:
        return


def checkPrice(drink, amount):
    cost = menu[drink]["cost"]

    if amount >= cost:
        change = round(amount - cost, 2)
        print(f"Here is your {drink}.\nAnd here is your change. ${change}")
    elif amount < cost:
        print("Sorry, that is not enough money.")


def deduct(drink, resource):
    ingrlist = ["water", "milk", "coffee"]
    total = menu[drink]["ingredients"]
    for i in ingrlist:
        resource[i] -= total[i]
    resource["money"] += menu[drink]["cost"]


while run == True:
    order = input("What would you like? espresso/latte/cappuccino? ")

    if order == "off":
        run = False
    elif order == "report":
        print(resources)
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        checkResources(drink=order, resource=resources)

        print("Please insert coins")
        q = int(input("how many quarters? "))
        d = int(input("how many dimes? "))
        n = int(input("how many nickels? "))
        p = int(input("how many pennies? "))
        total = (q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01)

        checkPrice(drink=order, amount=total)
        deduct(order, resource=resources)
    else:
        print("That is not on the menu.")
        exit()
