
from turtle import Turtle, Screen
import random

colour = ['red', 'green', 'yellow', 'blue', 'purple']
user = False
dinesh = Turtle()
dinnu = Turtle()
sai = Turtle()
jer = Turtle()
kar = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt='which colour turtle will win the race')
tuples = [dinesh, dinnu, sai, jer, kar]

if user_bet:
    user = True

y_axis = -100
for i in tuples:
    i.shape('turtle')
    i.color(colour[-1])
    i.penup()
    i.goto(-230, y_axis)
    y_axis += 50
    colour.pop()

while user:
    for i in tuples:
        if i.xcor() > 230:
            win = i.pencolor()
            user = False
            if win == user_bet:
                print('you win')
            else:
                print('better luck next time')
        i.forward(random.randint(0, 10))
screen.exitonclick()
