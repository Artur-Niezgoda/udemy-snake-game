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

class Scoreboard(Turtle):
    """Class to keep the score and display it on the screen.

    Attributes:
        score (int): The player's current score.
        highscore (int): The highest score achieved by the player.

    Methods:
        reset(): Compare score with highscore and replace if necessary, then reset the score.
        display_score(): Display the current score and highscore on the screen.
    """
    
    def __init__(self):
        """Create a Scoreboard object to display the current score and highscore."""
        
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 290)

    def reset(self):
        """Compare score with highscore and replace if necessary, then reset the score."""
        
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.display_score()

    def display_score(self):
        """Display the current score and highscore on the screen."""
        
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGN, font=FONT)

    

class Border(Turtle):
    """Class that creates visual borders

    Args:
        Turtle (class): superclass of Border class
    """
    CORNER_POSITIONS = ((290, 290), (290, -290), (-290, -290), (-290, 290))

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
        for item in positions:
            self.goto(item)
