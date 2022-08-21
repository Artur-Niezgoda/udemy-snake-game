from turtle import Screen
from scoreboard import Scoreboard, Border
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=640, height=640)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.display_score()
border = Border()



screen.update()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score += 1
        scoreboard.display_score()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() <-280 or snake.head.ycor() > 280:
        game_is_on = False
    

screen.exitonclick()