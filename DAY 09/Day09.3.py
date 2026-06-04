print("Welcome to the secret Auction Program.")
mydict = {}
highest_bid = 0
winner = ""

while True:
    name = input("What is your name? : ")
    bid = int(input("What's your bid? : $"))
    mydict[name] = bid

    askkk = input("Are there any bidders? Type 'yes' or 'no' : ")
    if askkk.lower() == "no":
        break
    else:
        print("\n" * 20)

# winner check AFTER loop
for i in mydict:
    if mydict[i] > highest_bid:
        highest_bid = mydict[i]
        winner = i

print(f"The winner is {winner} with a bid of ${highest_bid}")
print("All bids:", mydict)

   