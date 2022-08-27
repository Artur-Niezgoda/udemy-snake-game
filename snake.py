"""Create snake and animate it

Classes:
    Snake

Methods:
    create_snake()
        create initial snake
    add_segment(tuple)
        add a segment to a snake
    extend()
        extend snake when eats food
    reset()
        reset snake to the initial size and position
    up()
        turn up
    down()
        turn down
    left()
        turn left
    right()
        turn right
    
Constants:
    STARTING_POSITIONS
        gives coordinates for initial snake segments
    MOVE_DISTANCE
        distance that snakes moves each time
    UP, DOWN, LEFT, RIGHT
        angles for setting the head of the snake in order to turn
"""

from turtle import Turtle

# coordinates for initial segments of the snake
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# speed of the snake
MOVE_DISTANCE = 20
# angles for main directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    Create a snake object controllable by user

    Attributes:
        segments (list): holds the objects representing parts of snake's body
        create_snake (function): function creating snake's body 
        head (object): the first part of the snake
    """

    def __init__(self):
        """Construct all the necessary attributes for the object snake
        """

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def reset(self):
        """Reset the snake to its initial size and position"""
        
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head= self.segments[0]

    def create_snake(self):
        """Create parts of the snakes body
        """

        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
    
    def add_segment(self, position):
        """Create new Turtle object as a segment of the snake's body.

        Args:
            position (tuple): tuple of ints pointing to where the new segment
                              will be created
        """

        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Extend snake by adding one body segment at the end of the snake"""

        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move snake forward by telling each segment to follow the one in front"""

        for seg_num in range(len(self.segments)-1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num-1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """If the head is not going down, change direction of head to UP
        """

        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        """If the snake is not going up, change direction of head to DOWN
        """

        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        """If the snake is not going right, change direction of head to LEFT
        """

        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        """If the snake is not going left, change direction of head to RIGHT
        """

        if self.head.heading() != LEFT:    
            self.head.setheading(0)