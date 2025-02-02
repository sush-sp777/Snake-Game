from turtle import Turtle,Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time
import warnings
warnings.filterwarnings("ignore") 
screen=Screen() 
screen.setup(width=600,height=600) #this width and height is in pixel
screen.bgcolor("black") #screen background color
screen.title("Snake Game") # title of screen
screen.tracer(0)

snake= Snake()
food=Food()    #making food object
scoreboard=Scoreboard()
screen.listen()  #for listning the key strokes
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)  
    snake.move()
   

    #detect collision with food
    if snake.head.distance(food)<15:
       food.refresh()
       snake.extend()
       scoreboard.increase_score()
    
    #5detect collision with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        game_is_on=False
        scoreboard.game_over()
    
    #6detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass

        elif snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()

screen.exitonclick()