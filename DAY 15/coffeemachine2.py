from data import MENU, resources

is_true = True
profit = 0
resources["money"] = profit

def process_coins():
    print("Insert the coins")
    total = int(input("Quarters: ")) * 0.25
    total += int(input("Nickles: ")) * 0.05
    total += int(input("Pennies: ")) * 0.01
    total += int(input("Dimes: ")) * 0.10
    return total

def is_coin_enough(money_received, price):
    global profit
    if money_received >= price:
        change = round(money_received - price, 2)
        print(f"Money received, here is your change ${change}")
        profit += price
        resources["money"] = profit
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order):
    for item in order:
        resources[item] -= order[item]
    print(f"Here is your {drink_name}. Enjoy!")

while is_true:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_true = False

    elif choice == "report":
        for items in resources:
            print(f"{items}: {resources[items]}")

    else:
        drink = MENU[choice]
        drink_items = drink["ingredients"]

        # Check resources
        enough_resources = True
        for item in drink_items:
            if drink_items[item] > resources[item]:
                print(f"Sorry there is not enough {item}")
                enough_resources = False
                break

        if enough_resources:
            payment = process_coins()
            if is_coin_enough(payment, drink["cost"]):
                make_coffee(choice, drink_items)
