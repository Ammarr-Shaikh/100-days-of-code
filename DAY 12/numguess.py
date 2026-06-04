import random 
print(r"""
 _   _                 _                  ____                     
| \ | |               | |                / __ \                    
|  \| | _____      __ | |__   ___  ___  | |  | |_   _  ___  ___ ___ 
| . ` |/ _ \ \ /\ / / | '_ \ / _ \/ __| | |  | | | | |/ _ \/ __/ __|
| |\  |  __/\ V  V /  | | | |  __/\__ \ | |__| | |_| |  __/\__ \__ \
|_| \_|\___| \_/\_/   |_| |_|\___||___/  \____/ \__,_|\___||___/___/
                                                                    
""")

print("Welcome to the  Number Guessing Game!")
print("Choose the number between 1 to 100.")

level = input("Choose a difficulty. Type 'easy' or 'hard': " ).lower()
ans = random.randint(1,100)
def hard():   
    num_of_guess = 5
    while num_of_guess > 0:
        print(f"You have {num_of_guess} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == ans:
            print(f"You got it the answer was {ans}")
            break
        elif guess > ans:
            print("Too high.\nGuess again")
            num_of_guess -= 1
        elif guess < ans:
            print("Too low.\nGuess again")
            num_of_guess -= 1
        if num_of_guess == 0:
            print("You ran out of guesses.Game over")
def easy():
    num_of_guess = 10
    while num_of_guess > 0:
        print(f"You have {num_of_guess} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == ans:
            print(f"You got it the answer was {ans}")
            break
        elif guess > ans:
            print("Too high.\nGuess again")
            num_of_guess -= 1
        elif guess < ans:
            print("Too low.\nGuess again")
            num_of_guess -= 1
        if num_of_guess == 0:
            print("You ran out of guesses.Game over")
if level == "hard":
    hard()
else:
    easy()
