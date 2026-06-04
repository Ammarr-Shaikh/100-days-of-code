import random
def calculate_score(cards):
        score = sum(cards)
        while 11 in cards and score > 21:
                cards.remove(11)
                cards.append(1)
                score = sum(cards)
        return score
while True:
    user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if user_input != "y":
            print("Thanks for playing")
            break
    
    else:
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
        cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        users_card = random.choices(cards, k=2)
        computers_card = random.choices(cards,k=2)
        print(f"Your cards: {users_card} current score: {calculate_score(users_card)}")
        print(f"computer's first card: {computers_card[0]}")
        while calculate_score(users_card) < 21:
                ask = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                if ask == "y":
                    new_card = random.choice(cards)
                    users_card.append(new_card)
                    print(f"Your cards: {users_card} current score: {calculate_score(users_card)}")
                    print(f"computer's first card: {computers_card[0]}")
                else: break
    while calculate_score(computers_card) <=16:
                            newc_card = random.choice(cards)
                            computers_card.append(newc_card)
    print(f"Your cards: {users_card} current score: {calculate_score(users_card)}")
    print(f"computer's final cards: {computers_card} computer score {calculate_score(computers_card)}")

    user_score = calculate_score(users_card)
    comp_score = calculate_score(computers_card)
    def compare():
        if user_score> 21:
                return"You went over.You lose"
        elif comp_score>21:
                return"Computer went over.You win"
        elif comp_score ==21 and user_score == 21:
                return"both Black jack.Computer wins (house edge)"
        elif user_score == 21:
                return"Black jack.You win"
        elif user_score == comp_score:
                return"Draw"
        elif user_score > comp_score:
                return"You win "
        else:
                return"You lose"
    print(compare())
