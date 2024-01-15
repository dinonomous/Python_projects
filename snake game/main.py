from turtle import Screen
from food import Food
from snake import Snake
from scorebord import scorebord
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('my snake game')
screen.title("my snake game")
screen.tracer(0)
snake = Snake()
food = Food()
scorebord = scorebord()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    if (
            snake.segments[0].xcor() > 280
            or snake.segments[0].xcor() < -280
            or snake.segments[0].ycor() > 280
            or snake.segments[0].ycor() < -280
    ):
        scorebord.reseat()
        snake.reset()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scorebord.increse_score()


    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:

            scorebord.reseat()
            snake.reset()


screen.exitonclick()