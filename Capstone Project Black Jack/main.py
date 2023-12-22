import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def randcard():
  randomnumber=cards[random.randint(0,12)]
  return randomnumber
  
def who_win(player,computer):
  if sum(player)>sum(computer):
    print("You Win")
  elif sum(player)<sum(computer):
    print("You Lose")
  else:
    print("Draw")

def computer_choice(computer):
  initcom=computer
  random_choice=random.randint(0,1)
  if random_choice==0:
    computer.append(randcard())
    if sum(computer)>21:
      return initcom
    return computer
  else:
    return computer

player=[]
computer=[]


want_to_play=input("Do You Want To Play Black Jack 'YES' to play ").lower()
print(logo)
while(want_to_play=='yes'):
  for i in range(2):
    player.append(randcard())
    computer.append(randcard())
  
  print("Player Cards are ", player)
  print("Sum of Your Total Cards are",sum(player))
  print("computer cards are ", computer[1])

  if sum(player)==21 and len(player)==2:
    print("Black Jack! You Win")
    want_to_play=input("Do You Want To Play Again 'YES' to play ").lower()
    if want_to_play=='yes':
      continue
    else:
      break
  else:
    user=input("Do you want to draw a card yes or no : ").lower()
  
  while user=='yes':
      player.append(randcard())
      print("Player Cards are ", player)
      print("Sum of Your Total Cards are",sum(player))
      print("computer cards are ", computer)
      print("Sum of computer Total Cards are",sum(computer))
      if sum(player)>21:
        print("Your Sum Of Cards Are Grater Than 21 YOU LOSE")
        break
      elif sum(player)<21:
        computer=computer_choice(computer)
        if sum(computer)>21:
          print("Computer Exeded 21 You Win ")
          break
        user=input("Do you want to draw a card yes or no : ").lower()
      else:
        who_win(player,computer)
  else:
    print("computer cards are ", computer)
    print("Sum of computer Total Cards are",sum(computer))
    who_win(player,computer)

  want_to_play=input("Do You Want To Play Again 'YES' to play ").lower()