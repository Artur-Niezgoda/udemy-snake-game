from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("Blue")
        self.speed(0)
        self.refresh()
    
    

    def refresh(self):
        self.goto(random.randrange(-280, 300, 20), random.randrange(-280, 300, 20))
