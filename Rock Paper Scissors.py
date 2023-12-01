rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
game_lis=[rock,paper,scissors]
want_to_play=int(input("Do you want to play rock paper scissors? Type 1 for yes and 0\n"))
if want_to_play==1:
  while (want_to_play == 1):
    user_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    computer=random.randint(0,2)
    
    if user_input>=3 or user_input<0:
      print("You typed an invalid number, you lose!")
    
    elif user_input ==2 and computer==0:
      print(f"You lost {game_lis[user_input]} {game_lis[computer]}")
    
    elif user_input>computer:
      print(f"You win {game_lis[user_input]} {game_lis[computer]}")
      
    elif user_input==0 and computer==1:
      print(f"You lost {game_lis[user_input]} {game_lis[computer]}")
    
    elif user_input == 0 and computer == 2:
      print(f"You win {game_lis[user_input]} {game_lis[computer]}")
    
    elif computer == user_input:
      print(f"Its a draw {game_lis[user_input]} {game_lis[computer]}")
    
    else :
      print(f"You lost {game_lis[user_input]} {game_lis[computer]}")
  
    want_to_play=int(input("Do you want to play rock paper scissors? Type 1\n"))
    if want_to_play!=1:
      break


else:
  print("Thank you for playing")