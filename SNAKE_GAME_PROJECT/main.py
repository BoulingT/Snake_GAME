from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

#Screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

#Snake settings
snake = Snake()
#Food settings
food = Food()
#Score settings
score = ScoreBoard()

#Control settings
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#Game condition
game_is_on = True

#Game
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    #Detect collision with the wall
    if (snake.head.xcor() > 280) or (snake.head.xcor() < -280) or (snake.head.ycor() > 280) or (snake.head.ycor() < -280):
        game_is_on = False
        score.game_over()

    #Detect collision with tail
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            score.game_over()


screen.exitonclick()
