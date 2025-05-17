############ NOTE !!!! ##########
# Set interpreter: 3.9.7('base') conda or 3.8.2

# https://stackoverflow.com/questions/600293/how-to-check-if-a-number-is-a-power-of-2

# ----------- 4 layer flower ----------

import turtle

num_petals = int(input('--> Enter the number of petal(8 16 32 64...2 to the power): '))

while (num_petals < 8 or (num_petals & (num_petals -1) != 0)):
    if num_petals < 8:
        print("number of petals must be at least 8.")
    elif (num_petals & (num_petals -1) != 0):
        print("number must be the power of 2.")
    num_petals = int(input('Enter the number of petal(8 16 32 64...2 to the power): '))

flower_size = int(input('--> Enter the size of flower(50-200): '))

while(flower_size < 50 or flower_size > 200):
    print("flower size must be between 50 to 200")
    flower_size = int(input('Enter the size of flower(50-200): '))

arc_length = 90
radius = flower_size
radius_decrement = flower_size / 4

# ------- Turtle drawing:
t = turtle.Turtle()
screen = turtle.Screen()

t.pensize(1)
t.pencolor("aquamarine")
t.speed(20)

for j in range(4): # 4 layers of the flower
    if j % 2 == 0:
        t.fillcolor('oldlace')
    else:
        t.fillcolor('pink')
    print("Layer ", j + 1)
    for i in range(num_petals):
        t.begin_fill()
        t.circle(radius,arc_length)
        t.left(90)
        t.circle(radius,arc_length)
        t.end_fill()
        t.right(360/num_petals)
        
        if i == num_petals -1:
            print("last petal ", i+1, "at layer ", j + 1)
    radius -= radius_decrement

screen.exitonclick() #keep window open until it's terminated
# t.mainloop() #this will keep graphic window opened until window it's terminated