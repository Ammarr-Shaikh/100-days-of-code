import random
print("What do you choose? ")
choise = int(input("Type 1 for rock, 2 for paper or 3 for scissor: "))
rock ='''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissor='''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

if choise == 1:
    print(rock)
elif choise == 2:
    print(paper)
elif  choise == 3:
    print(scissor)
else: 
    print("invalid input")

my_list = [rock,paper,scissor]
computer_choice = random.choice(my_list)
print("Computer chose: \n")
print(computer_choice)
# if (computer_choice == my_list[0] and choise ==1) or (computer_choice == my_list[1] and choise ==2) or (computer_choice == my_list[2] and choise ==3):
#     print("Draw")
if (computer_choice == my_list[0] and choise == 2) or (computer_choice == my_list[1] and choise == 3) or (computer_choice == my_list[2] and choise == 1):
    print("You win")
elif (computer_choice == my_list[0] and choise == 3) or (computer_choice == my_list[1] and choise == 1) or (computer_choice == my_list[2] and choise == 2):
    print("Computer wins")
else:
    print("draw")