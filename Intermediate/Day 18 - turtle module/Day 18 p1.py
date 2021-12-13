import turtle as t
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")
timmy.shapesize(2, 2, 2)

t.colormode(255)

def ran_col():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    new_color = (r,g,b)
    return new_color






angle = [0, 90, 180, 270]
#timmy.pensize(10)
timmy.speed("fastest")

while True:
    timmy.circle(100)
    head = timmy.heading()
    timmy.setheading(head+10)
    timmy.circle(100)
    timmy.color(ran_col())













screen = Screen()
screen.exitonclick()
