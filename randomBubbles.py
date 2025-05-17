############ NOTE !!!! ##########
# Set interpreter: 3.9.7('base') conda or 3.8.2

# ----------- Random Bubbles ----------
import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()

screen.screensize(800,600)
t.pensize(1)
t.pencolor("aquamarine")
t.speed(10)

print(random, type(random))

for i in range(10):
    rand_x_axis = random.randint(-500, 800)
    
    rand_y_axis = random.randint(-500, 600)
    

    print(rand_x_axis, " ", rand_y_axis)

# while(rand_x_axis != -350):
    





screen.exitonclick() #keep window open until it's terminated
# t.mainloop() #this will keep graphic window opened until window it's terminated