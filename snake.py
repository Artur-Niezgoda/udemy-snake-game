from turtle import Turtle

INIT_NO = 3
MOVE_DISTANCE = 20

class Snake:
    """_summary_
    """

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

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
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)
        # if key == "Left":
        #     self.segments[0].setheading(180)
        # if key == "Down":
        #     self.segments[0].setheading(270)
        # if key == "Right":
        #     self.segments[0].setheading(0)