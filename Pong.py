# Pong game in python 3!

# Import statements
import turtle


# Setting up the window
window = turtle.Screen()
window.title("Pong game by Alex:")
window.bgcolor("black")
window.setup(width=800, height=600)
# Stops the window from updating (Speeds up game)
window.tracer(0)


# Player 1
player_1 = turtle.Turtle()

# Sets animation speed for turtle module
player_1.speed(0)

# Sets the shape and color of the paddle
player_1.shape("square")
player_1.color("white")
player_1.shapesize(stretch_wid=5, stretch_len=1)
player_1.penup()
# Left side of screen.
player_1.goto(-350, 0)


# Player 2
player_2 = turtle.Turtle()
player_2.speed(0)
player_2.shape("square")
player_2.color("white")
player_2.shapesize(stretch_wid=5, stretch_len=1)
player_2.penup()
# Right side of screen.
player_2.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)


# Function definition for players
def player_1_up():
    y = player_1.ycor()
    y += 20
    player_1.sety(y)

def player_1_down():
    y = player_1.ycor()
    y -= 20
    player_1.sety(y)

def player_2_up():
    y = player_2.ycor()
    y += 20
    player_2.sety(y)

def player_2_down():
    y = player_2.ycor()
    y -= 20
    player_2.sety(y)
# Keyboard binding
window.listen()

# When user presses 'w' key the player moves up with function call
window.onkeypress(player_1_up, "w")
window.onkeypress(player_1_down, "s")
window.onkeypress(player_2_up, "Up")
window.onkeypress(player_2_down, "Down")

# Main game loop

while True:
    window.update()




