from turtle import Screen
from scoreboard import Scoreboard, Border
from snake import Snake
from food import Food
import time

# Create screen
screen = Screen()
screen.setup(width=640, height=640)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

# Call all classes
snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.display_score()
border = Border()


# Screen update after creating snake and key rules:
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
    snake.move()  # snake moves constantly

    # Snake eating food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score += 1
        scoreboard.display_score()
        snake.extend()
    
    # Collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        scoreboard.reset()
        snake.reset()

    # Collision with body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
