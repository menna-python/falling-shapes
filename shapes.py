from turtle import Turtle
import random
class Shapes(Turtle):
    def __init__(self):
        super().__init__()
        t_shapes=["square","circle","triangle","turtle"]
        colors=["red","green","blue","orange","white"]
        self.shape(random.choice(t_shapes))
        self.color(random.choice(colors))
        self.shapesize(0.75,0.75)
        self.penup()
        self.determine_position()
        self.dy=10

    def determine_position(self):
        x_range=random.randint(-270,270)
        self.goto(x_range,290)