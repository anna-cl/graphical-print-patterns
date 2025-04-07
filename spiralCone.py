# use csil machines to run
# https://www2.cs.sfu.ca/~wsumner/accessing-csil-remotely.html
# https://www.sfu.ca/fas/computing/support/csil/unix/cpu-servers.html
# python spiralCone.py

# https://github.com/asweigart/simple-turtle-tutorial-for-python/blob/master/draw_circles.py

from turtle import *

# maxRadius = int(input('Enter the max radius: '))
# minRadius = int(input('Enter the min radius: '))
# numCircles = int(input('Enter number of circles: '))

t = turtle.Turtle()

# t.bgcolor("pink")
t.penup()
t.goto(0, -150)
t.pendown()

t.pensize(2)
t.pencolor(169, 169, 255)
t.speed(6)

minRadius = 2
maxRadius = 120
input = 20

for i in range(input):
  if i == 0:
    t.circle(minRadius)
  elif (i == input -1):
    t.circle(maxRadius)
  else:
    t.circle(minRadius*i + (maxRadius-minRadius)/(input-2)) #this dividing does NOT create each circle in correct proportion 
  
  t.penup()
  t.left(90)
  t.forward(10)
  t.right(90)
  t.pendown()
	