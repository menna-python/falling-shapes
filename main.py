from turtle import Screen
from paddle import Paddle
from shapes import Shapes
from scoreboard import Scoreboard
import time
import turtle

# Create the game window
window = Screen()
window.bgcolor("black")
window.title("Falling Bricks")
window.setup(width=600, height=600)

# Global game control flag
game_on = True
window_closed = False  # Flag to track if the window is already closed

# Function to handle window close event
def on_close():
    global game_on, window_closed
    if not window_closed:  # Prevent multiple calls to close the window
        game_on = False  # Stop the game loop
        window_closed = True  # Mark the window as closed
        try:
            window.bye()  # Close the Turtle window
        except turtle.Terminator:
            pass  # Ignore errors if the window is already closed

# Bind the window close protocol to the on_close function
window.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", on_close)

# Disable automatic screen updates
window.tracer(0)

# Initialize game objects
paddle = Paddle()
score = Scoreboard()

# Set up keyboard controls
window.listen()
window.onkey(paddle.right, "Right")
window.onkey(paddle.left, "Left")

try:
    default_sleep = 0.07  # Initial delay between updates

    while game_on:  # Main game loop
        # Create a new falling shape
        s = Shapes()

        # Control the shape's falling motion
        while game_on and s.ycor() > -290:
            s.goto(s.xcor(), s.ycor() - s.dy)  # Move the shape down
            window.update()
            time.sleep(default_sleep)

            # Check for collision with the paddle
            if s.ycor() == paddle.ycor() and s.distance(paddle) <= 30:
                s.hideturtle()
                if s.shape() == "square":
                    score.update_score(2)
                elif s.shape() == "triangle":
                    score.clear()
                    score.score = 0
                    score.show_score()
                elif s.shape() == "turtle":
                    if s.fillcolor() == "white" and s.pencolor() == "white":
                        score.clear()
                        score.game_over()
                        window.update()
                        time.sleep(3)
                        on_close()  # Trigger game closure
                    else:
                        score.update_score(5)
                else:
                    score.update_score(1)

            # Hide the shape if it falls below the paddle
            elif s.ycor() < paddle.ycor():
                s.hideturtle()

        default_sleep *= 0.9  # Speed up the game slightly

except turtle.Terminator:
    pass  # Handle window closure gracefully

#finally:
    # Ensure the window is closed properly
    #if not window_closed:  # Close the window only if it's still open
       # try:
           # window.bye()
        #except turtle.Terminator:
            #pass
