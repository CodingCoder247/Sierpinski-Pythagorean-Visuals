'''
Name: Syarifah Radhiyah D/O Mohd Rafi
Admin Number: 231816M
Tutorial Group: IT1312-02
Question: 2a(iii)
Description: Pythagoras Tree Right Lean
'''

import turtle  # Import the turtle graphics library for drawing
import math  # Import the math library for mathematical operations


# Draw a single square of the given size, and fill it in
def drawSquare(t, size, color):
    t.begin_fill()  # Begin filling the square with color
    t.fillcolor(color)
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()  # End filling the square


# Draw a node at the given level, recursively drawing all the smaller nodes
def drawNode(t, size, level, use_multi_color):
    if level < 1:  # Base case: stop recursion when level is less than 1
        return
    else:
        if use_multi_color:
            # Use a different color for each level
            color = level_colors[level - 1]
        else:
            # Use a single color
            color = single_color
        drawSquare(t, size, color)  # Draw the square at the current level

        # Draw the left branch
        leftSize = size / 2
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.right(120)
        t.forward(leftSize)
        t.left(90)
        drawNode(t, leftSize, level - 1, use_multi_color)  # Recursively draw the left branch with a smaller size

        # Draw the right branch
        rightSize = size * math.sqrt(3) / 2
        t.right(180)
        t.forward(rightSize)
        t.left(90)
        drawNode(t, rightSize, level - 1, use_multi_color)  # Recursively draw the right branch with a smaller size
        t.left(30)
        t.back(size)


# Prompt the user to choose between multi-colour and single-color
user_choice = input("Do you want a multi-coloured tree? [Y/N]: ").upper()

if user_choice == "Y":
    use_multi_color = True
    # Define a list of colors for each level
    level_colors = ["#f9c1c9", "#ffe4e1", "#ffb6c1", "#ff9eb5", "#ff85a5", "#ff6b93", "#ff577f", "#ff416c"]
else:
    use_multi_color = False
    # Use a single color
    single_color = "#f9c1c9"

screen = turtle.Screen()
screen.bgcolor("sky blue")
# This turns screen updates off
screen.tracer(0)  # Turn off automatic screen updates

myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.speed(0)

# Position the turtle, and start drawing!
myTurtle.penup()
myTurtle.goto(-35, -150)
myTurtle.left(90)
myTurtle.pendown()

# Indicate the size of the tree and the number of levels
drawNode(myTurtle, 80, 8, use_multi_color)  # Draw the tree with initial parameters

myTurtle.hideturtle()

# Update the screen to see the changes
screen.update()

# Close the turtle graphics window on click
screen.exitonclick()
