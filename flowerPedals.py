# https://stackoverflow.com/questions/600293/how-to-check-if-a-number-is-a-power-of-2

# import turtle
# import math

num_petals = int(input('Enter the number of petal(8 16 32 64...2 to the power): '))

while (num_petals < 8 or (num_petals & (num_petals -1) != 0)):
    if num_petals < 8:
        print("number of petals must be at least 8.")
    elif (num_petals & (num_petals -1) != 0):
        print("number must be the power of 2.")
    num_petals = int(input('Enter the number of petal(8 16 32 64...2 to the power): '))

flower_size = int(input('Enter the size of flower(50-200): '))

