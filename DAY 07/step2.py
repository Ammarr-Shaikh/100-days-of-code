import random
word_list = ["aardvark", "camel","baboon"]

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
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
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ""
for ch in chosen_word:
    placeholder += "_"
print(placeholder)
game_over = False
while not game_over:
    guess = input("Guess a letter: ").lower()
    display =""
    for ch in chosen_word:
        if ch == guess:
            display = display+ ch
        else:
            display +="_"
    print(display)
