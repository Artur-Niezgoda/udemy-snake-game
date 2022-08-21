from turtle import Turtle

INIT_NO = 3
MOVE_DISTANCE = 20

class Snake:
    """_summary_
    """

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(INIT_NO):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.setx(-i*20)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num-1].pos())
        self.segments[0].forward(MOVE_DISTANCE)