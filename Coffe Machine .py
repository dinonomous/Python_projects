MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "cost" : 0
}

def calcutate_ingredients(request):
  for item in MENU[request]["ingredients"]:
    resources[item] -= MENU[request]["ingredients"][item]
    if "cost" not in resources:
      resources["cost"].append(MENU[request]["cost"])
    else:
      resources["cost"] += MENU[request]["cost"]



def check_resources(request):
  for item in MENU[request]["ingredients"]:
    if resources[item] < MENU[request]["ingredients"][item]:
      print(f"Sorry there is not enough {item}.")
      return False
  return True
  
request = True
while(request):
  request=input("What do you want to drink (espresso/latte/cappuccino)").lower()
  if request == "off":
    request=False
    break
  elif request=="report":
    print(resources)
  else:
    if check_resources(request):
      print("Please insert coins.")
      quarters = int(input("How many quarters?"))
      dimes = int(input("How many dimes?"))
      nickles = int(input("How many nickles?"))
      pennies = int(input("How many pennies?"))
      total = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
      if total >= MENU[request]["cost"]:
        print(f"Here is ${round(total-MENU[request]['cost'],2)} in change.")
        print(f"Here is your {request} ☕️. Enjoy!")
        calcutate_ingredients(request)
      else:
        print("Sorry that's not enough money. Money refunded.")