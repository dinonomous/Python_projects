import art
from game_data import data 
import random
import os


score = 0
deleted_list=[]
next=[]
winlose=True

def clear():
    # Check the operating system and clear the screen accordingly
    if os.name == 'posix':
        # For Linux and MacOS
        os.system('clear')
    elif os.name == 'nt':
        # For Windows
        os.system('cls')

def random_choice():
  rand_index = random.randint(0, len(data) - 1)
  return data.pop(rand_index)
  
def main():
  print(art.logo)
  global winlose
  if len(next)==0:
    choice_1 = random_choice()
  else:
    choice_1 = next[-1]
    
  print(f"competitor A : {choice_1['name']} {choice_1['description']} from {choice_1['country']}")
  print(art.vs)
  choice_2 = random_choice()
  print(f"competitor B : {choice_2['name']} {choice_2['description']} from {choice_2['country']}")
  next.append(choice_2)
  winlose=compare(choice_1['follower_count'],choice_2['follower_count'])
  

def compare(follow1,follow2):
  temp=input("Select who has more follower's A or B : ").lower()
  if temp=='a':
    if follow1>follow2:
      return True
    else:
      return False
  elif temp=='b':
    if follow1<follow2:
      return True
    else:
      return False
    

while(winlose):
  print(f"your score is {score}")
  main()
  if (winlose):
    score+=1
  else:
    print("You lose ")
    print(f"your score was {score}")
    break
  clear()
  