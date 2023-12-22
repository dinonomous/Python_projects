from art import logo
def add(num1,num2):
  number=num1+num2
  return number
def sub(num1,num2):
  number=num1-num2
  return number
def multiply(num1,num2):
  number=num1*num2
  return number
def devide(num1,num2):
  number=num1/num2
  return number

operations={
  '+':add,
  '-':sub,
  '*':multiply,
  '/':devide,
}

print(logo)

def calculator():
  user=True
  num1='0'
  num2='0'
  
  while(num1.isnumeric()):
    num1=input("type your first number : ")
    if num1.isnumeric():
      num1=int(num1)
      break
    else:
      print("Type A Valid Number")
      num1='0'
    
  while(num2.isnumeric()):
    num2=input("type your second number : ")
    if num2.isnumeric():
      num2=int(num2)
      break
    else:
      print("Type A Valid Number")
      num2='0'
      
  user_input=''
  while user_input not in operations.keys():
      for i in operations:
          print(i)
      user_input = input("Pick an Operation From Above : ")
      if user_input in operations.keys():
          break
      else:
          print("Select from the provided operations")
          user_input=''
    
  
  calculation_function=operations[user_input]
  answer=calculation_function(num1,num2)
  print(f"{num1} {user_input} {num2} = {answer}")
  
  while(user):
  
    num3=input("Do you want to calculate another number to the answer ? : if yes type the number or no : ")
    if num3.isalpha():
      user=False
      break
    elif num3.isnumeric():
      for i in operations:
        print(i)
      user_input=input("Pick an Operation From Above : ")
      calculation_function=operations[user_input]
      answer2=calculation_function(answer,int(num3))
      print(f"{answer} {user_input} {num3} = {answer2}")

  again=input("Do you want to calculate with new numbers type y or n to exit : ")
  if again=='y':
    calculator()
  else:
    return
calculator()