from project import data
from project import logo
from project import vs
import random
print(logo)
A = random.choice(data)
B = random.choice(data)
compA = "COmpare A: "
compB = "Against B: "
choice_A = f" {A["name"]}, a {A['description']}, from {A['country']}."
print(compA + choice_A)
print(vs)
choice_B = f" {B["name"]}, a {B['description']}, from {B['country']}."
score = 0
print(compB + choice_B)
if choice_A == choice_B:
    print("it cannot be compared. Please restart the game")
else:
    while True:
        ok = input("Who has more followers? Type 'A' or 'B': ")
        if ok == "A" and A["follower_count"] > B["follower_count"]:  
            A = B
            choice_A = choice_B
            B = random.choice(data)

            choice_B = f" {B["name"]}, a {B['description']}, from {B['country']}."
            if A==B:
               print("it cannot be compared. Please restart the game")
               break
            else:
                score +=1
                print(f"You're right! Current score: {score}")
                print(compA + choice_A)
                print(vs)
                print(compB + choice_B)
           
        elif ok == "B" and B["follower_count"] > A["follower_count"]:
            A = B
            choice_A = choice_B
            B = random.choice(data)

            choice_B = f" {B["name"]}, a {B['description']}, from {B['country']}."
            if A==B:
               print("it cannot be compared. Please restart the game")
               break
            else:
                score += 1
                print(f"You're right! Current score: {score}")
                print(compA + choice_A)
                print(vs)
                print(compB + choice_B) 
             
        else: 
            print(f"Sorry that's wrong. Final score: {score}")
            break

        