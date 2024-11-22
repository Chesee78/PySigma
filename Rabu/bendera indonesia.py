import turtle

def drawRectangle(ttl, x, y, width, height, color):
    """Draw a filled rectangle with the given color."""
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    ttl.fillcolor(color)
    ttl.begin_fill()
    for _ in range(2):
        ttl.forward(width)
        ttl.right(90)
        ttl.forward(height)
        ttl.right(90)
    ttl.end_fill()
    ttl.penup()


screen = turtle.Screen()
screen.bgcolor("sky blue")

pen = turtle.Turtle()
pen.pensize(2)
pen.speed(3)


drawRectangle(pen, -150, 100, 300, 100, "red")

drawRectangle(pen, -150, 0, 300, 100, "white")


pen.hideturtle()


turtle.done()