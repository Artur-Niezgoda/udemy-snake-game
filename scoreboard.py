"""The module to keep the score and display in on the screen.

Classes:
    Scoreboard(Turtle)
    Border(Turtle)

Methods:
    reset()
        Compare score with highscore and replace if that's the case, then reset the score
    display_score()
        Display score and highscore on top of the screen

Constants:
    ALIGN
        option for aligning score text
    FONT
        tuple containing font, fontsize and font option
    CORNER_POSITIONS
        tuple containing positions of the corners, use to draw border
"""

from turtle import Turtle

# option for aligning score text
ALIGN = "center"
# tuple containing font, fontsize and font option
FONT = ("Times New Roman", 20, "bold")
# tuple containing positions of the corners, use to draw border
CORNER_POSITIONS = ((290, 290), (290, -290), (-290, -290), (-290, 290))

class Scoreboard(Turtle):
    """Class creating a score text on the top of the screen

    Args:
        Turtle (class): superclass of Scoreboard class

    Attributes:
        score (int): initial score, default 0 
        highscore (int): highest score ever achieved
    """
    def __init__(self):
        """Creates object that displays score
        """

        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 290)

    # def game_over(self):
    #     """Display 'Game Over' and ends the game when snake hits wall or tail
    #     """

    #     self.goto(0,0)
    #     self.write("Game Over", align="center", font=("Times New Roman", 20, "bold"))

    def reset(self):
        """Compare score with highscore and replace if that's the case, then reset the score
        """
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.display_score()

    def display_score(self):
        """Display score and highscore on top of the screen"""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Times New Roman", 20, "bold"))

    

class Border(Turtle):
    """Class that creates visual borders

    Args:
        Turtle (class): superclass of Border class
    """
    def __init__(self, positions=CORNER_POSITIONS):
        """Create visual borders, which crossing causes the end of game

        Args:
            positions (tuple, optional): contain tuples of int standing for
            each corner of the border to be drawn. Defaults to CORNER_POSITIONS.
        """
        
        super().__init__()
        self.color("grey")
        self.hideturtle()
        self.penup()
        self.goto(-290, 290)
        self.pendown()
        for item in (positions):
            self.goto(item)