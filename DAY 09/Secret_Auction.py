print("Welcome to the secret auction program.")
my_dict = {}
highest_bid = 0
winner = ""
while True:
    name = input("Whats is your name? : ")
    bid = int(input("Whats your bid? : $"))
    my_dict[name] = bid
    askkk = input("Are there any other bidders? Type 'yes' or 'no': ")
    if askkk == "no":
        break
    else:
        print("\n")

for i in my_dict:
    if my_dict[i] > highest_bid:
        highest_bid = my_dict[i]
        winner = i
print(f"The winner is {winner} with bid ${highest_bid}")