"""The module contains Food class that creates randomly piece of food every time
snake eats it.

Classes:
    Food(Turtle)

Methods:
    refresh()
        Create food in random place on the screen
"""


from turtle import Turtle
import random

class Food(Turtle):
    """Create food object on the map in random localisation

    Args:
        Turtle (class): superclass of Food class
    """

    def __init__(self):
        """Create an object and asign its attributes
        """
        
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("Blue")
        self.speed(0)
        self.refresh()
    
    

    def refresh(self):
        """Create food in random place on the screen
        """

        self.goto(random.randrange(-280, 300, 20), random.randrange(-280, 300, 20))
