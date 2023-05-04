import math
import random
import turtle

sc = turtle.Screen()
sc.update()
sc.bgcolor('black')
sc.setup(width=1000, height=600)

left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("white")
left_pad.shapesize(stretch_wid=4, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("white")
right_pad.shapesize(stretch_wid=4, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

hit_ball = turtle.Turtle()
hit_ball.speed(100)
hit_ball.shape("square")
hit_ball.color("white")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = 0

powerDown = turtle.Turtle()
powerDown.shape('triangle')
powerDown.shapesize(stretch_wid=2)
powerDown.color('white')
powerDown.penup()
powerDown.goto(random.randint(-100, 100), random.randint(-100, 100))
cheatfunctions = ['shrink', 'speed']

left_player = 0
right_player = 0

sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("white")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)

sketch.write("Left_player : 0    Right_player: 0", align="center", font=("Courier", 24, "italic"))



sc.listen()
sc.onkeypress(lambda: left_pad.sety(left_pad.ycor() + 20), "w")
sc.onkeypress(lambda: left_pad.sety(left_pad.ycor() - 20), "s")
sc.onkeypress(lambda: right_pad.sety(right_pad.ycor() + 20), "Up")
sc.onkeypress(lambda: right_pad.sety(right_pad.ycor() - 20), "Down")


def colision(ballX, ballY, powerDownX, powerDownY):
    distance = math.sqrt(math.pow((ballX - powerDownX), 2) + math.pow((ballY - powerDownY), 2))
    if distance <= hit_ball.__sizeof__() + powerDown.__sizeof__():
        randomChoice = random.choice(cheatfunctions)
        print(randomChoice)
        powerDown.clear()
        powerDown.goto(random.randint(-100, 100), random.randint(-100, 100))
        if randomChoice == 'speed':
            hit_ball.speed(100)
        else:
            if ballX < 0:
                left_pad.shapesize(stretch_wid=2, stretch_len=1)
                sc.update()
            else:
                right_pad.shapesize(stretch_wid=2, stretch_len=1)
                sc.update()


while True:
    sc.update()
    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1

    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy = 1

    if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor() + 40 and hit_ball.ycor() > right_pad.ycor() - 40):
        hit_ball.speed(40)
        right_pad.shapesize(stretch_wid=4, stretch_len=1)
        hit_ball.setx(360)
        hit_ball.dx *= -1
        hit_ball.dy = random.randint(-1, 5)
        hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    if (hit_ball.xcor() < -360 and hit_ball.xcor() > -370) and hit_ball.ycor() < left_pad.ycor() + 40 and (hit_ball.ycor() > left_pad.ycor() - 40):
        hit_ball.speed(40)
        left_pad.shapesize(stretch_wid=4, stretch_len=1)
        hit_ball.setx(-360)
        hit_ball.dx = 5
        hit_ball.dy = random.randint(-1, 5)
        hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))

    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        right_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
            left_player, right_player), align="center",
            font=("Courier", 24, "normal"))
    colision(hit_ball.xcor(), hit_ball.ycor(), powerDown.xcor(), powerDown.ycor())
W