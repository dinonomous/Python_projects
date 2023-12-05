from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.

print(art.logo)

members={}

def addtodictionary(name,bid):
  members[name]=bid

next=True
while(next):
  name=input("What is Your name : ")
  bid = int(input("How much do you want to bid :$"))
  addtodictionary(name,bid)
  x=input("is there any another person? ")
  if x == 'yes':
    next=True
  else:
    next=False
  clear()
max=0
key=''
for i in members:
  if members[i]>max:
    max=members[i]
    key=i

print(f"the highest bid is {key} and bid is {max}")