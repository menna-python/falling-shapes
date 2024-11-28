from turtle import Turtle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.color("white")
        self.penup()
        self.goto(0,-270)

    def right(self):
        new_x=self.xcor()+60
        if new_x<250:
            self.goto(new_x,self.ycor())

    def left(self):
       new_x=self.xcor()-60
       if new_x>-250:
            self.goto(new_x,self.ycor())
