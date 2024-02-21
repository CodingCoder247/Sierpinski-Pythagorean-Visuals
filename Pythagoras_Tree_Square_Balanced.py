import turtle  # Import the turtle graphics library for drawing
import math  # Import the math library for mathematical operations


# Function to draw a single square of the given size and fill it in
def drawSquare(t, size):
    t.begin_fill()  # Begin filling the square with color
    for i in range(4):
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
        leftSize = math.sqrt(size * size / 2)
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.right(135)
        t.forward(leftSize)
        t.left(90)
        drawNode(t, leftSize, level - 1)  # Recursively draw the left branch with a smaller size

        # Draw the right branch
        rightSize = math.sqrt(size * size / 2)
        t.right(180)
        t.forward(rightSize)
        t.left(90)
        drawNode(t, rightSize, level - 1)  # Recursively draw the right branch with a smaller size
        t.left(45)
        t.back(size)


# Function to draw a filled circle with the specified radius and color
def filled_circle(radius, color):
    turtle.begin_fill()
    turtle.color(color)
    turtle.circle(radius)
    turtle.end_fill()


# Function to draw a rainbow with specified radius and interval
def rainbow(radius, interval):
    roygbiv = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'lightblue']

    turtle.penup()
    turtle.goto(0, -radius)  # Adjust the starting position of the rainbow
    turtle.pendown()

    for r_color in roygbiv:
        filled_circle(radius, r_color)
        radius -= interval

        # Move turtle up by a little
        turtle.left(90)
        turtle.forward(interval)
        turtle.right(90)


# Function to set up the turtle for drawing the tree
def setup_tree_turtle():
    myTurtle = turtle.Turtle()
    myTurtle.shape("turtle")
    myTurtle.color("black")
    myTurtle.fillcolor("yellow")
    myTurtle.speed(1)

    myTurtle.penup()
    myTurtle.goto(45, -150)  # Adjust the position to prevent overlapping with the rainbow
    myTurtle.left(90)
    myTurtle.pendown()

    return myTurtle


# Main function to draw the tree and rainbow based on user input
def main():
    add_rainbow = input("Add a magic rainbow [Y/N]: ").upper()

    screen = turtle.Screen()
    screen.bgcolor("cyan")
    screen.tracer(0)  # Turn off automatic screen updates

    myTreeTurtle = setup_tree_turtle()

    if add_rainbow == 'Y':
        rainbow(300, 10)

    drawNode(myTreeTurtle, 80, 8)  # Draw the tree with initial parameters

    myTreeTurtle.hideturtle()
    screen.update()  # Update the screen with the final drawing

    turtle.exitonclick()  # Close the turtle graphics window when clicked


# Run the main function
main()
