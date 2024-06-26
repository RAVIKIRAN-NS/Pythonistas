from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)#the default shape of turtleis 20,20 ,so it will bemultiplied(100,20)
        self.penup()
        self.goto(position)
        self.speed(0)


    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
