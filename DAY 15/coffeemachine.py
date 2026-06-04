from data import MENU, resources
def insert_coins():
    print("Insert the coins")
    quarter = int(input("Quarters: "))
    nickle =  int(input("nickles: "))
    penny =  int(input("pennies: "))
    dime =  int(input("dimes: "))
    total = quarter*(0.25) + nickle*(0.05) + penny*(0.01) + dime*(0.10)
    return round(total,2)
espresso = MENU["espresso"]
espresso_ingridient = espresso["ingredients"]
latte = MENU["latte"]
latte_ingridient = latte["ingredients"]
cappuccino = MENU["cappuccino"]
cappuccino_ingridient = cappuccino["ingredients"]
resources["money"] = 0


while True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()    
    if user_input == "espresso":
        
        if resources["water"] >= espresso_ingridient["water"] and resources["coffee"] >= espresso_ingridient["coffee"]:
            total = insert_coins()
            resources["money"] += total
            if total >= espresso["cost"]:
                total_money = total - espresso["cost"]
                if total_money > 0:
                    print(f"Here is ${round(total_money,2)} dollars in change")
                    
                
                print(f"Here is your {user_input}.Enjoy!")
                water_left = resources["water"] - espresso_ingridient["water"]
                coffee_left = resources["coffee"] - espresso_ingridient["coffee"]
                resources["water"] = water_left
                resources["coffee"] =coffee_left
            else:
                print("Sorry that's not enough money. Money refunded.")
            
        else: 
            if resources["water"] < espresso_ingridient["water"]:
                print("sorry there is not enough water")
            else:
                print("sorry there is not enough coffee")

    elif user_input == "latte":
        
        if resources["water"] >= latte_ingridient["water"] and resources["coffee"] >= latte_ingridient["coffee"] and resources["milk"] >= latte_ingridient["milk"]:
            total = insert_coins()
            resources["money"] += total
            if total >= latte["cost"]:
                total_money = total - latte["cost"]
                if total_money > 0:
                    print(f"Here is ${round(total_money,2)} dollars in change")
                    
                
                print(f"Here is your {user_input}.Enjoy!")
                water_left = resources["water"] - latte_ingridient["water"]
                coffee_left = resources["coffee"] - latte_ingridient["coffee"]
                milk_left = resources["milk"] - latte_ingridient["milk"]
                resources["water"] = water_left
                resources["coffee"] =coffee_left
                resources["milk"] = milk_left
            else:
                print("Sorry that's not enough money. Money refunded.")
            
        else: 
            if resources["water"] < latte_ingridient["water"]:
                print("sorry there is not enough water")
            elif resources["milk"] < latte_ingridient["milk"]:
                print("sorry there is not enough milk")
            else:
                print("sorry there is not enough coffee")
    elif user_input == "cappuccino":
          
        if resources["water"] >= cappuccino_ingridient["water"] and resources["coffee"] >= cappuccino_ingridient["coffee"] and resources["milk"] >= cappuccino_ingridient["milk"]:
            total = insert_coins()
            resources["money"] += total
            if total >= cappuccino["cost"]:
                total_money = total - cappuccino["cost"]
                if total_money > 0:
                    print(f"Here is ${round(total_money,2)} dollars in change")
                    
                
                print(f"Here is your {user_input}.Enjoy!")
                water_left = resources["water"] - cappuccino_ingridient["water"]
                coffee_left = resources["coffee"] - cappuccino_ingridient["coffee"]
                milk_left = resources["milk"] - cappuccino_ingridient["milk"]
                resources["water"] = water_left
                resources["coffee"] =coffee_left
                resources["milk"] = milk_left
            else:
                print("Sorry that's not enough money. Money refunded.")
            
        else: 
            if resources["water"] < cappuccino_ingridient["water"]:
                print("sorry there is not enough water")
            elif resources["milk"] < cappuccino_ingridient["milk"]:
                print("sorry there is not enough milk")
            else:
                print("sorry there is not enough coffee")


    elif user_input == "report":
        for i in resources:
            print(i,":",resources[i])
    else: 
        print("Machine turned off")
        break
