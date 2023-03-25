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

# Set up key bindings for controlling the snake's direction
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

    # Move the snake forward
    snake.move()

    # Check if the snake has eaten the food
    if snake.head.distance(food) < 15:
        # Refresh the food and update the score
        food.refresh()
        scoreboard.score += 1
        scoreboard.display_score()
        snake.extend()
    
    # Check if the snake has collided with the walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        # Reset the score and snake if it has collided
        scoreboard.reset()
        snake.reset()

    # Check if the snake has collided with its own body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # Reset the score and snake if it has collided
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
