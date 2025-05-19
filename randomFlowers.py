############ NOTE !!!! ##########
# Set interpreter: 3.9.7('base') conda or 3.8.2

# ----------- Random Flowers ----------
import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()

screen.screensize(800,600)
t.pensize(1)
t.pencolor("aquamarine")
t.speed(15)


t.penup()
t.home()
t.shape("turtle")
t.shapesize(2, 2)

screen.exitonclick() #keep window open until it's terminated
