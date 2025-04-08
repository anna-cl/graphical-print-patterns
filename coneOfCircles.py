# set interpreter: 3.9.7('base') conda or 3.8.2
# https://github.com/asweigart/simple-turtle-tutorial-for-python/blob/master/draw_circles.py

import turtle
import math

minRadius = int(input('Enter the min radius: '))
maxRadius = int(input('Enter the max radius: '))
num_circles = int(input('Enter number of circles: '))

t = turtle.Turtle()
screen = turtle.Screen()

# t.bgcolor("pink")
t.penup()
t.goto(-120, -150)
t.pendown()

t.pensize(2)
# t.pencolor(169, 169, 255)
t.pencolor("purple")
t.speed(15)

# minRadius = 2
# maxRadius = 120
# num_circles = 20

last_i = num_circles
first_i = 1

'''
Let's assume y is radius and x is i(index of circles):
first, use linear equation to find the slope(the radius increment of each circle)
m = (maxRadius - minRadius) / (last_i - first_i)
second, find c(height) to locate where the line graph on matrix
y = mx + c --> radius = m * i + c 
'''

#find slope, first and last circles are known:
m = (maxRadius - minRadius) / (last_i - first_i)
# find height of the line graph:
c = minRadius - m * 1 #use first circle; we can also use last circle to find c 

# == First cone of circles:
for i in range(1, num_circles + 1):
  if i == 1:
    t.circle(minRadius)
  elif (i == num_circles + 1):
    t.circle(maxRadius)
  else:
    t.circle(m * i + c)
    # t.circle(minRadius*i + (maxRadius-minRadius)/(num_circles-2)) #this dividing does NOT create each circle in correct proportion 

  t.penup()
  t.left(90)
  t.forward(5)
  t.right(90)
  t.pendown()

# == Second cone of cicirles:
t.penup()
t.goto(130, -150)
t.pendown()
t.pencolor("green")

for i in range(1, num_circles + 1):
  t.circle(m * i + c)

  t.penup()
  t.left(90)
  t.forward(5)
  t.right(90)
  t.pendown()
  print("circle ", i, " radius is ", math.ceil( m*i+c))
	
screen.exitonclick() #keep window open until it's terminated
t.mainloop() #this will keep graphic window opened until window it's terminated