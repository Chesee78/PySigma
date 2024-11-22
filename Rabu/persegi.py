import turtle

def drawRectangle(ttl, x, y, width, height):
    """Draw a rectangle of dimensions width and height, with upper left corner at (x, y)."""
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    for _ in range(2):
        ttl.forward(width)
        ttl.right(90)
        ttl.forward(height)
        ttl.right(90)
    ttl.penup()

screen = turtle.Screen()
screen.bgcolor("white")


pen = turtle.Turtle()
pen.pensize(2)
pen.color("red")


drawRectangle(pen, -50, 50, 200, 100)


pen.hideturtle()

turtle.done()