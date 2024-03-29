from turtle import Turtle
POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
tim = Turtle()
UP = 90
DOWN =270
LEFT = 180
RIGHT= 0

class Snake:

    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]

    def create_snake(self):
        for new_pos in POSITION:
            self.add_turtle(new_pos)

    def add_turtle(self,position):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.all_turtles.append(tim)

    def reset(self):
        for turtless in self.all_turtles:
            turtless.goto(1000,1000)
        self.all_turtles.clear()
        self.create_snake()
        self.head = self.all_turtles[0]

    def extend_turtle(self):
        self.add_turtle(self.all_turtles[-1].position())
        #this line returns the position of last turtle

    def move(self):
        for tur_num in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[tur_num - 1].xcor()
            new_y = self.all_turtles[tur_num - 1].ycor()
            self.all_turtles[tur_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

