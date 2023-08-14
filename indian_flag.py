import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("lightpink")

# Create the turtle object
flag = turtle.Turtle()
flag.speed(0)
flag.penup()
flag.goto(-250, 150)
flag.pendown()

# Draw the saffron color (top stripe)
flag.color("#FF9933")
flag.begin_fill()
for _ in range(2):
    flag.forward(500)
    flag.right(90)
    flag.forward(50)
    flag.right(90)
flag.end_fill()

# Move to the white stripe
flag.penup()
flag.goto(-250, 100)
flag.pendown()

# Draw the white stripe
flag.color("white")
flag.begin_fill()
for _ in range(2):
    flag.forward(500)
    flag.right(90)
    flag.forward(50)
    flag.right(90)
flag.end_fill()

# Draw the Ashoka Chakra
flag.penup()
flag.goto(-0, 0)
flag.pendown()

# Ashoka Chakra Color and Redius
radius = 20
flag.color("blue", "blue")


# Draw the 24 spokes of the Ashoka Chakra
flag.penup()
flag.goto(-20, 75)
flag.pendown()
flag.pensize(2)
for _ in range(24):
    flag.forward(radius)
    flag.backward(radius)
    flag.left(360 / 24)

# Move to the green rectangle
flag.penup()
flag.goto(-250, 50)
flag.pendown()

# Draw the green rectangle
flag.color("#138808")
flag.begin_fill()
for _ in range(2):
    flag.forward(500)
    flag.right(90)
    flag.forward(50)
    flag.right(90)
flag.end_fill()

# Hide the turtle
flag.hideturtle()

# Keep the window open until it's closed by the user
turtle.done()
