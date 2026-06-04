print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
split= int(input("How many people split the bill? "))
tipper = tip/100
Final_bill = (bill + (bill*tipper))/split
print("Each person should pay: $",round(Final_bill,2)) 