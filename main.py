from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
#600x600 pixels
screen.setup(width=600, height=600)
screen.bgcolor("darkgreen")
screen.title("Serpentine")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
edge = 285
negative_edge = -285

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    #detect collision with food.
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.shed_skin()
        scoreboard.keep_score()
    
    #detect collision with edge
    if snake.head.xcor() > edge or snake.head.ycor() > edge or snake.head.xcor() < negative_edge or snake.head.ycor() < negative_edge:
        scoreboard.reset()
        snake.reset()
    
    #detect collision 'self'
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 5:
            scoreboard.reset()
            snake.reset()








screen.exitonclick()