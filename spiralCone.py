# use csil machines to run
# https://www2.cs.sfu.ca/~wsumner/accessing-csil-remotely.html
# https://www.sfu.ca/fas/computing/support/csil/unix/cpu-servers.html
# python spiralCone.py

# https://github.com/asweigart/simple-turtle-tutorial-for-python/blob/master/draw_circles.py

from turtle import *
from tkinter import *
from tkinter import ttk

# maxRadius = int(input('Enter the max radius: '))
# minRadius = int(input('Enter the min radius: '))
# numCircles = int(input('Enter number of circles: '))

t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

t.pensize(2)

minRadius = 2
maxRadius = 120
input = 5
for i in range(input + 1):
  if i >= 1:
		t.circle(maxRadius / i + minRadius )
