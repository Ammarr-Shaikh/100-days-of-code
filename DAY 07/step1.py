import random
word_list = ["aardvark", "camel","baboon"]
chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("Guess a letter: ")
guessed_word = ""
for i in chosen_word:
    if i == guess:
        print("right")
    else: 
        print("Wrong")    