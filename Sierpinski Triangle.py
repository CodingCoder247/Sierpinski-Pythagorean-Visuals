import turtle


# Function to draw a filled triangle given three points and a colour
def drawTriangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()  # Pen up
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()  # Pen down
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.end_fill()


# Function to calculate the midpoint between two points
def getMid(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


# Recursive function to draw Sierpinski triangles
def sierpinski(points, degree, myTurtle):
    # Colours to be added to diagram in order
    colors = ['blue', 'red', 'green', 'cyan', 'yellow', 'magenta']
    drawTriangle(points, colors[degree], myTurtle)
    if degree > 0:
        sierpinski([points[0],
                    getMid(points[0], points[1]),
                    getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                    getMid(points[0], points[1]),
                    getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                    getMid(points[2], points[1]),
                    getMid(points[0], points[2])],
                   degree-1, myTurtle)


# Main function to set up the turtle and initiate the drawing
def main():
    myTurtle = turtle.Turtle()
    # Adjust the drawing speed here
    myTurtle.speed(10)
    myWin = turtle.Screen()

    # 3 points of the first triangle based on [x, y] coordinates
    myPoints = [[-200, -50], [0, 200], [200, -50]]

    # Vary the degree of complexity here
    degree = 5

    # First call of the recursive function
    sierpinski(myPoints, degree, myTurtle)

    # Hide the turtle cursor after drawing is completed
    myTurtle.hideturtle()

    # Exit program when user clicks on the window
    myWin.exitonclick()


# Call the main function
main()
