from turtle import Turtle


class scorebord(Turtle):
    def __init__(self):
        super().__init__()
        self.SCORE = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scorebord()
        self.hideturtle()

    def update_scorebord(self):
        self.clear()
        self.write("Score :{} High Score : {}".format(self.SCORE,self.highscore), align="center", font=("arial", 10, "bold"))

    def increse_score(self):
        self.SCORE += 1
        self.update_scorebord()

    #def gameover(self):
     #   self.color("white")
      #  self.penup()
       # self.goto(0, 0)
        #self.write("game OVER you score was:{}".format(self.SCORE), align="center", font=("arial", 15, "bold"))

    def reseat(self):

        if self.SCORE > self.highscore:
            self.highscore = self.SCORE
            with open("data.txt", mode='w') as file:
                file.write(f'{self.highscore}')
        self.SCORE = 0
        self.update_scorebord()
