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
t.speed(20)

# for i in range(10):
#     rand_x_axis = random.randint(-800, 800)
    
#     rand_y_axis = random.randint(-600, 600)
    
#     print(rand_x_axis, " ", rand_y_axis)

# 41 colors:
colorlist = ["black", "grey", "darkgrey", "lightcoral", "brown", "maroon", "red", "tomato", "orangered", "saddlebrown", "peru",
             "darkorange", "tan", "wheat", "goldenrod", "gold", "khaki", "olive", "yellow", "greenyellow", "limegreen", "green",
             "aquamarine", "lightseagreen", "paleturquoise", "teal", "cyan", "skyblue", "dodgerblue", "royalblue", "lavender", 
             "navy", "blue", "blueviolet", "darkviolet", "purple", "fuchsia", "deeppink", "hotpink", "crimson", "pink"]

print("colors: ", len(colorlist))

t.penup()
t.goto(-300, 150)
t.pendown()
for i in range(len(colorlist)):
    t.fillcolor(colorlist[i])
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.penup()
    t.forward(25)
    t.pendown()

# while(rand_x_axis != -350):
#     # random location:
#     rand_x_axis = random.randint(-800, 800)
#     rand_y_axis = random.randint(-600, 600)
#     print(rand_x_axis, " ", rand_y_axis)

#     #random size:
#     random.randint(10,100)






screen.exitonclick() #keep window open until it's terminated
# t.mainloop() #this will keep graphic window opened until window it's terminated