from turtle import Turtle
starting_position=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments=[]
        self.create_snake()
        self.head= self.segments[0]

    def create_snake(self):          #1. here snake body is created
        for position in starting_position:
            self.add_segment(position)
           
    
    def move(self):                  #2. here snake is move
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num -1].xcor()
            new_y=self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self,position):
            new_segment=Turtle('square')
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)   
            self.segments.append(new_segment)
    def extend(self):                #4.adding new segment to snake (here snake is bigger and bigger)
        self.add_segment(self.segments[-1].position())
    
    def up(self):                     #3 moving the snake
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
