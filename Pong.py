import turtle
import os
import time
import random

wn = turtle.Screen()
wn.title("Pong by Davis Burrill")
wn.bgcolor("green")
wn.setup(width=1000, height=750)
wn.tracer(0)

# Players
player_a = turtle.textinput("Player A", "Name of Player A: ")
player_b = turtle.textinput("Player B", "Name of Player B: ")

# Score
score_a = 0
score_b = 0

# Game Over
game_over = False

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-450, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(450, 0)

# Paddle Movement Default
paddle_a.move_up = False
paddle_a.move_down = False
paddle_b.move_up = False
paddle_b.move_down = False

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2
ball_colors = ["white", "black", "red"]
ball_direction = [-3, -2, -1, 1, 2, 3]

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-400, -325)
pen.write(player_a, align="center", font=("Courier", 24, "normal"))
pen.goto(400, -325)
pen.write(player_b, align="center", font=("Courier", 24, "normal"))
pen.goto(-250, 275)
pen.write("0", align="center", font=("Courier", 72, "bold"))
pen.goto(250, 275)
pen.write("0", align="center", font=("Courier", 72, "bold"))
pen.goto(0, -325)
pen.write("First to 3 wins!", align="center", font=("Courier", 24, "normal"))



# Function

def paddle_a_up_start():
    paddle_a.move_up = True

def paddle_a_up_end():
    paddle_a.move_up = False

def paddle_a_down_start():
    paddle_a.move_down = True

def paddle_a_down_end():
    paddle_a.move_down = False

def paddle_b_up_start():
    paddle_b.move_up = True

def paddle_b_up_end():
    paddle_b.move_up = False

def paddle_b_down_start():
    paddle_b.move_down = True

def paddle_b_down_end():
    paddle_b.move_down = False


def writing():
    pen.goto(-400, -325)
    pen.write(player_a, align="center", font=("Courier", 24, "normal"))
    pen.goto(400, -325)
    pen.write(player_b, align="center", font=("Courier", 24, "normal"))
    pen.goto(-250, 275)
    pen.write(score_a, align="center", font=("Courier", 72, "bold"))
    pen.goto(250, 275)
    pen.write(score_b, align="center", font=("Courier", 72, "bold"))
    pen.goto(0, -325)
    pen.write("First to 3 wins!", align="center", font=("Courier", 24, "normal"))

# Keyboard binding
wn.listen()

wn.onkeypress(paddle_a_up_start, "w")
wn.onkeyrelease(paddle_a_up_end, "w")

wn.onkeypress(paddle_a_up_start, "W")
wn.onkeyrelease(paddle_a_up_end, "W")

wn.onkeypress(paddle_a_down_start, "s")
wn.onkeyrelease(paddle_a_down_end, "s")

wn.onkeypress(paddle_a_down_start, "S")
wn.onkeyrelease(paddle_a_down_end, "S")

wn.onkeypress(paddle_b_up_start, "Up")
wn.onkeyrelease(paddle_b_up_end, "Up")

wn.onkeypress(paddle_b_down_start, "Down")
wn.onkeyrelease(paddle_b_down_end, "Down")


#main game loop
while game_over == False:

    if paddle_a.move_up:
        if paddle_a.ycor() + 50 < 375:
            y = paddle_a.ycor()
            y += 10
            paddle_a.sety(y)

    if paddle_a.move_down:
        if paddle_a.ycor() - 50 > -375:
            y = paddle_a.ycor()
            y -= 10
            paddle_a.sety(y)

    if paddle_b.move_up:
        if paddle_b.ycor() + 50 < 375:
            y = paddle_b.ycor()
            y += 10
            paddle_b.sety(y)

    if paddle_b.move_down:
        if paddle_b.ycor() - 50 > -375:
            y = paddle_b.ycor()
            y -= 10
            paddle_b.sety(y)


    wn.update()

    # Move Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 365:
        ball.sety(365)
        ball.dy *= -1
        os.system("afplay hit.wav&")


    if ball.ycor() < -365:
        ball.sety(-365)
        ball.dy *= -1
        os.system("afplay hit.wav&")


    if ball.xcor() > 490:
        ball.goto(0, 0)
        ball.color(random.choice(ball_colors))
        ball.dx = 2
        ball.dy = random.choice(ball_direction)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.color("white")
        writing()
        os.system("afplay score.wav&")

    if ball.xcor() < -490:
        ball.goto(0, 0)
        ball.color(random.choice(ball_colors))
        ball.dx = -2
        ball.dy = random.choice(ball_direction)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.color("white")
        writing()
        os.system("afplay score.wav&")


    # Paddle and ball collisions

    if ball.xcor() > 440 and ball.xcor() < 450 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() + 27):
        ball.setx(440)
        ball.dx *= -1.24
        ball.dy = random.randint(4,5)
        os.system("afplay hit.wav&")
        print(ball.dy)

    if ball.xcor() > 440 and ball.xcor() < 450 and (ball.ycor() < paddle_b.ycor() + 27 and ball.ycor() > paddle_b.ycor() + 4):
        ball.setx(440)
        ball.dx *= -1.24
        ball.dy = random.randint(1,3)
        os.system("afplay hit.wav&")
        print(ball.dy)

    if ball.xcor() > 440 and ball.xcor() < 450 and (ball.ycor() < paddle_b.ycor() + 4 and ball.ycor() > paddle_b.ycor() - 4):
        ball.setx(440)
        ball.dx *= -1.24
        ball.dy = random.randint(-1,1)
        os.system("afplay hit.wav&")
        print(ball.dy)

    if ball.xcor() > 440 and ball.xcor() < 450 and (ball.ycor() < paddle_b.ycor() - 4 and ball.ycor() > paddle_b.ycor() - 27):
        ball.setx(440)
        ball.dx *= -1.24
        ball.dy = random.randint(-3,-1)
        os.system("afplay hit.wav&")
        print(ball.dy)

    if ball.xcor() > 440 and ball.xcor() < 450 and (ball.ycor() < paddle_b.ycor() - 27 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(440)
        ball.dx *= -1.24
        ball.dy = random.randint(-5,-4)
        os.system("afplay hit.wav&")
        print(ball.dy)

    if ball.xcor() < -440 and ball.xcor() > -450 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() + 27):
        ball.setx(-440)
        ball.dx *= -1.24
        ball.dy = random.randint(4,5)
        os.system("afplay hit.wav&")
        print(ball.dy)

    if ball.xcor() < -440 and ball.xcor() > -450 and (ball.ycor() < paddle_a.ycor() + 27 and ball.ycor() > paddle_a.ycor() + 4):
        ball.setx(-440)
        ball.dx *= -1.24
        ball.dy = random.randint(1,3)
        os.system("afplay hit.wav&")
        print(ball.dy)

    if ball.xcor() < -440 and ball.xcor() > -450 and (ball.ycor() < paddle_a.ycor() + 4 and ball.ycor() > paddle_a.ycor() - 4):
        ball.setx(-440)
        ball.dx *= -1.24
        ball.dy = random.randint(-1,1)
        os.system("afplay hit.wav&")
        print(ball.dy)

    if ball.xcor() < -440 and ball.xcor() > -450 and (ball.ycor() < paddle_a.ycor() - 4 and ball.ycor() > paddle_a.ycor() - 27):
        ball.setx(-440)
        ball.dx *= -1.24
        ball.dy = random.randint(-3,-1)
        os.system("afplay hit.wav&")
        print(ball.dy)

    if ball.xcor() < -440 and ball.xcor() > -450 and (ball.ycor() < paddle_a.ycor() - 27 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-440)
        ball.dx *= -1.24
        ball.dy = random.randint(-5,-4)
        os.system("afplay hit.wav&")
        print(ball.dy)

    # Victory Condition

    if score_a == 3:
        os.system("afplay win.wav&")
        pen.goto(0,0)
        pen.color("white")
        pen.write(player_a + " Wins!!", align="center", font=("Courier", 72, "bold"))
        time.sleep(5)
        game_over = True
        os.system("killall afplay")
    elif score_b == 3:
        os.system("afplay win.wav&")
        pen.goto(0,0)
        pen.color("white")
        pen.write(player_b + " Wins!!", align="center", font=("Courier", 72, "bold"))
        time.sleep(5)
        game_over = True
        os.system("killall afplay")





