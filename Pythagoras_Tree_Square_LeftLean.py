'''
Name: Syarifah Radhiyah D/O Mohd Rafi
Admin Number: 231816M
Tutorial Group: IT1312-02
Question: 2a(ii)
Description: Pythagoras Tree Left Lean
'''

import turtle  # Import the turtle graphics library for drawing
import math  # Import the math library for mathematical operations


# Function to draw a single square of the given size and fill it
def drawSquare(t, size):
    t.begin_fill()  # Begin filling the square with color
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()  # End filling the square


# Function to draw a node at the given level, recursively drawing all the smaller nodes
def drawNode(t, size, level):
    if level < 1:  # Base case: stop recursion when level is less than 1
        return
    else:
        drawSquare(t, size)  # Draw the square at the current level

        # Draw the left branch
        leftSize = size * math.sqrt(3) / 2
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.right(150)
        t.forward(leftSize)
        t.left(90)
        drawNode(t, leftSize, level - 1)  # Recursively draw the left branch with a smaller size

        # Draw the right branch
        rightSize = size / 2
        t.right(180)
        t.forward(rightSize)
        t.left(90)
        drawNode(t, rightSize, level - 1)  # Recursively draw the right branch with a smaller size
        t.left(60)
        t.back(size)


# Function to draw clouds
def filled_circle(radius, color):
    turtle.color(color, color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


# Function to draw a single cloud
def cloud(radius, cloud_color="white"):
    filled_circle(radius, cloud_color)
    turtle.forward(radius)
    filled_circle(radius, cloud_color)
    turtle.right(90)
    filled_circle(radius, cloud_color)
    turtle.right(90)
    filled_circle(radius, cloud_color)
    turtle.right(90)
    filled_circle(radius, cloud_color)
    turtle.right(90)


# Prompt user for input
cloud_choice = input("Add fluffy clouds [Y/N]: ").upper()

# Initialise turtle
screen = turtle.Screen()
screen.bgcolor("sky blue")
screen.tracer(0)  # Turn off automatic screen updates

myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.color("black")
myTurtle.fillcolor("#91e891")
myTurtle.speed(0)

# Draw the tree
myTurtle.penup()
myTurtle.goto(120, -150)
myTurtle.left(90)
myTurtle.pendown()
drawNode(myTurtle, 80, 10)  # Draw the tree with initial parameters
myTurtle.hideturtle()

# Draw clouds if user chooses 'Y' or 'y'
if cloud_choice == 'Y':
    turtle.penup()
    # Cloud positions
    turtle.goto(5, 225)
    cloud(15)
    turtle.goto(100, 250)
    cloud(25)
    turtle.goto(190, 200)
    cloud(15)
    turtle.goto(-150, 250)
    cloud(20)
    turtle.goto(275, 200)
    cloud(25)
    turtle.goto(-275, 200)
    cloud(30)

# Update the screen to see the changes
screen.update()

# Close the turtle graphics window on click
screen.exitonclick()
