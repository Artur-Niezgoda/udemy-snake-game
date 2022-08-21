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
        self.goto(0, 270)

        
    def display_score(self):
        self.clear()
        self.write("Dcore: "+ str(self.score), align="center", font=("Times New Roman", 20, "bold"))