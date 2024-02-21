import turtle


# Function to draw a filled square given four points and a colour
def drawSquare(points, color, myTurtle, show=False):
    if show:
        print('DRAW:', points)

    myTurtle.fillcolor(color)
    myTurtle.up()  # Pen up
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()  # Pen down
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[3][0], points[3][1])
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.end_fill()


# Function to calculate the new point given two points and vertical/horizontal parameters
def get(p1, p2, V, H, show=False):  # Vertical, Horizontal
    x1, y1 = p1
    x2, y2 = p2

    dx = x2 - x1
    dy = y2 - y1

    new_x = x1 + V/3 * dx
    new_y = y1 + H/3 * dy

    if show:
        print('NEW:', new_x, new_y)

    return new_x, new_y


# Recursive function to draw Sierpinski squares
def sierpinski(points, degree, myTurtle):

    colormap = ['blue', 'red', 'green', 'cyan', 'yellow',
                'violet', 'orange']

    # Draw a square based on the 4 points given
    drawSquare(points, colormap[degree], myTurtle)

    # Draw 8 smaller squares within the current square
    if degree > 0:
        # Plot square 1 of 8
        sierpinski([
            get(points[0], points[2], 0, 0),
            get(points[0], points[2], 0, 1),
            get(points[0], points[2], 1, 1),
            get(points[0], points[2], 1, 0)
        ], degree-1, myTurtle)

        # Plot square 2 of 8
        sierpinski([
            get(points[0], points[2], 0, 1),
            get(points[0], points[2], 0, 2),
            get(points[0], points[2], 1, 2),
            get(points[0], points[2], 1, 1)
        ], degree - 1, myTurtle)

        # Plot square 3 of 8
        sierpinski([
            get(points[0], points[2], 0, 2),
            get(points[0], points[2], 0, 3),
            get(points[0], points[2], 1, 3),
            get(points[0], points[2], 1, 2)
        ], degree - 1, myTurtle)

        # Plot square 4 of 8
        sierpinski([
            get(points[0], points[2], 1, 2),
            get(points[0], points[2], 1, 3),
            get(points[0], points[2], 2, 3),
            get(points[0], points[2], 2, 2)
        ], degree - 1, myTurtle)

        # Plot square 5 of 8
        sierpinski([
            get(points[0], points[2], 2, 2),
            get(points[0], points[2], 2, 3),
            get(points[0], points[2], 3, 3),
            get(points[0], points[2], 3, 2)
        ], degree - 1, myTurtle)

        # Plot square 6 of 8
        sierpinski([
            get(points[0], points[2], 2, 1),
            get(points[0], points[2], 2, 2),
            get(points[0], points[2], 3, 2),
            get(points[0], points[2], 3, 1)
        ], degree - 1, myTurtle)

        # Plot square 7 of 8
        sierpinski([
            get(points[0], points[2], 2, 0),
            get(points[0], points[2], 2, 1),
            get(points[0], points[2], 3, 1),
            get(points[0], points[2], 3, 0)
        ], degree - 1, myTurtle)

        # Plot square 8 of 8
        sierpinski([
            get(points[0], points[2], 1, 0),
            get(points[0], points[2], 1, 1),
            get(points[0], points[2], 2, 1),
            get(points[0], points[2], 2, 0)
        ], degree - 1, myTurtle)


# Main function to set up the turtle and initiate the drawing
def main():
    myTurtle = turtle.Turtle()
    myTurtle.speed(10)  # Adjust the drawing speed here
    myWin = turtle.Screen()

    # 4 points of the first square based on [x,y] coordinates
    myPoints = [[0, 0], [0, 200], [200, 200], [200, 0]]

    # Vary the degree of complexity here
    degree = 4

    # First call of the recursive function
    sierpinski(myPoints, degree, myTurtle)

    # Hide the turtle cursor after drawing is completed
    myTurtle.hideturtle()

    # Exit program when user click on window
    myWin.exitonclick()


main()
