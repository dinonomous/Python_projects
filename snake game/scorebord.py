from turtle import Turtle

class scorebord(Turtle):
    def __init__(self):
        super().__init__()
        self.SCORE = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scorebord()
        self.hideturtle()

    def update_scorebord(self):
        self.write("Score :{}".format(self.SCORE), align="center", font=("arial", 10, "bold"))
    def increse_score(self):
        self.SCORE += 1
        self.clear()
        self.update_scorebord()

    def gameover(self):
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.write("game OVER you score was:{}".format(self.SCORE), align="center", font=("arial", 15, "bold"))