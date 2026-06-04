import random
words = [
    "aardvark","camel", "baboon"
]
HANGMANPICS = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']


lives = 5
# Hangman ASCII banner
print(r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                
''')

chosen_word = random.choice(words)
print(chosen_word)

placeholder = ""
for i in chosen_word:
        placeholder += "_"
print(placeholder)
game_over = False
list = []
while not game_over:
    print(f"*************************{lives}/5 Lives left****************************")
   
    
    guess = input("guess a letter: ").lower()
    display = ""
    if guess in list:
        print("you have already guessed: ",guess)
    for letter in chosen_word:
        if letter == guess:
            display += guess
            list.append(guess)
        elif letter in list:
            display+= letter
        else:
            display+= "_"
    print(display)
    # if letter not in chosen_word:
    #     print("The letter you guessed: ",guess)
    #     print("You lose a life")
    #     lives-=1
    if  guess not in  chosen_word:
        lives-=1
        print(f"You have  guessed a wromg word: {guess} \nYou lose a life")
        if lives ==0:
            game_over = True
            print("game over")
            print("You lose")
     
    
    if "_" not in display:
        game_over = True
        print("You won")
    print(HANGMANPICS[lives])