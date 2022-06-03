import turtle
import time
import random

delay = .1

score = 0
high_score = 0

window = turtle.screen()
window.title("snake game")
window.background("black")
window.setup(width=600, height=600)
window.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("blue")
head.penup()
head.goto(0, 0)
head.direction = 'stop'

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("triangle")
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(100, 260)
pen.write("score = 0 , high score = 0 ", align="center", font=("Courier", 24, "normal"))


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


window.listen()
window.onkeypress(go_up, 'w')
window.onkeypress(go_down, 's')
window.onkeypress(go_left, 'a')
window.onkeypress(go_right, 'd')

while True:
    window.update()

    if head.xcor() > 290 or head.xcor() < - 290 or head.ycor() > 290 or head.ycor() < - 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

        score = 0
        delay = .1