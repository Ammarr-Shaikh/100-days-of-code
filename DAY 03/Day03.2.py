print("Welcome to the python pizza deliveries!")
size = input("Whats the size you need S, M or L? ")
pepperani = input("Do you want pepperani on pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill+=20
elif size == "L":
    bill+=25

else:
    print("Invalid input")

if pepperani == "Y":
    if size =="S":
        bill +=2
    else: 
        bill +=3
else:
    pass

if extra_cheese == "Y":
    bill +=1

print("Your total bill to be paid: ", bill)