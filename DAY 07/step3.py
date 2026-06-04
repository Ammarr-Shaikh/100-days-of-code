import random
word_list = ["aardvark", "camel","baboon"]
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ""
for ch in chosen_word:
    placeholder += "_"
print(placeholder)
n = len(chosen_word)
display =[]
while n >= 0:
   
 
    guess = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                 display[i] = guess
            else:
                 pass
                #  display[i] = "_"
                 
print(display)

# while n >0:
#     
    
#     for ch in chosen_word:
#         if chosen_word == guess:
#             display[ch]= guess
#         else:
#             display[ch]= "_"
#     print("".join(display))
#     n-= 1