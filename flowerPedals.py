############ NOTE !!!! ##########
# Set interpreter: 3.9.7('base') conda or 3.8.2

# https://stackoverflow.com/questions/600293/how-to-check-if-a-number-is-a-power-of-2

import turtle
import math

num_petals = int(input('Enter the number of petal(8 16 32 64...2 to the power): '))

while (num_petals < 8 or (num_petals & (num_petals -1) != 0)):
    if num_petals < 8:
        print("number of petals must be at least 8.")
    elif (num_petals & (num_petals -1) != 0):
        print("number must be the power of 2.")
    num_petals = int(input('Enter the number of petal(8 16 32 64...2 to the power): '))

flower_size = int(input('Enter the size of flower(50-200): '))

# ------- Turtle drawing:
t = turtle.Turtle()
screen = turtle.Screen()

t.pensize(2)
# t.pencolor(169, 169, 255)
t.pencolor("pink")
t.speed(5)

t.fillcolor('yellow')
t.begin_fill()
t.circle(100,90)
t.left(90)
t.circle(100,90)
t.end_fill()
t.right(360/num_petals)


screen.exitonclick() #keep window open until it's terminated
t.mainloop() #this will keep graphic window opened until window it's terminated