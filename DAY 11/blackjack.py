import random
print(r"""
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                 
                      |__/                  
""")
while True:
    play_game = input("Do u want to play a game of blackjack? Type 'y' for yes or 'n' for no. : ")
    if play_game != "y":
        break
    cards = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]
    your_cards = random.choices(cards,k=2)
    sum = 0
    for i in your_cards:
        sum+=i
    print(f"Your cards: {your_cards} Current Score: {sum}")
    computers_first_caard = random.choice(cards)
    print(f"Computer's first card: {computers_first_caard}")
    zum =0
    num_choices = random.choice([2,3,4])
    computer_cards = random.sample(cards, num_choices)
    for i in computer_cards:
        zum += i

    if sum <= 21:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == "y":
            new_card = random.choice(cards)
            your_cards.append(new_card)
            sum += new_card
            print(f"Your cards: {your_cards} Current Score: {sum}")
            print(f"Computer's first card: {computers_first_caard}")
            
        elif another_card == "n":
            print(f"Your cards: {your_cards} Final Score: {sum}")
           
            print(f"Computer's final hand: {computer_cards} Final score: {zum}")
            

        else:
            print(f"Your cards: {your_cards} Current Score: {sum}")
            print(f"Computer's final card: {computers_first_caard} final score: {computers_first_caard}")



        if sum == 21:
                print("Black jack.You win")
        elif zum == 21:
                print("Black jack . computer wins")
        elif sum ==  zum or sum == computers_first_caard:
                print("Draw")
        elif sum <21 and (sum > computers_first_caard or  sum > zum):
                print("you win")
        elif sum > 21:
                print("You went over. you lose")
        elif zum > 21:
                print("you won")          
        else:
                print("Computer wins")
