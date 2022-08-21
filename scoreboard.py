from turtle import Turtle
ALIGN = "center"
FONT = ("Times New Roman", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.shape()
        self.penup()
        self.hideturtle()
        self.goto(0, 290)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Times New Roman", 20, "bold"))
        
    def display_score(self):
        self.clear()
        self.write("Score: "+ str(self.score), align="center", font=("Times New Roman", 20, "bold"))

    

class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.color("grey")
        self.hideturtle()
        self.penup()
        self.goto(-290, 290)
        self.pendown()
        for item in ((290, 290), (290, -290), (-290, -290), (-290, 290)):
            self.goto(item)