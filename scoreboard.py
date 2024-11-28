from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.score=0
        self.show_score()

    def show_score(self):
        self.write(f"Score:{self.score}",font={"courier",32,"bold"})

    def game_over(self):
        self.clear()
        self.goto(-50,0)
        self.write(f"Game over\nFinal score:{self.score}",font={"courier",32,"bold"})

    def update_score(self,n):
        self.score+=n
        self.clear()
        self.show_score()

   