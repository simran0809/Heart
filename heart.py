import math
from turtle import *

# Define the x-coordinate of the heart
def hearta(k):
    return 15 * math.sin(k) ** 3

# Define the y-coordinate of the heart
def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# Set up the turtle
speed(0)
bgcolor("black")
pensize(2)
penup()
goto(0, 0)
pendown()

# Draw the glowing heart effect
colors = ["#ffcccc", "#ff99aa", "#ff6688", "#ff3366", "#f73487"]  # Lighter to darker shades

for shade in range(len(colors)):
    color(colors[shade])
    for i in range(1000):
        x = hearta(i / 100) * (20 - shade)  # Adjust size slightly for each layer
        y = heartb(i / 100) * (20 - shade)
        goto(x, y)
    penup()  # Lift the pen to avoid lines when moving to the next heart layer
    goto(0, 0)
    pendown()

# Keep the window open
done()
