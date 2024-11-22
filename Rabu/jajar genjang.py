import turtle

def drawParallelogram(ttl, x, y, side_length, angle):
    """Draw a parallelogram starting at (x, y) with the given side length and angle."""
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    for _ in range(2):
        ttl.forward(side_length)
        ttl.left(angle)
        ttl.forward(side_length)
        ttl.left(180 - angle)
    ttl.penup()

screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.pensize(2)
pen.color("blue")

drawParallelogram(pen, -50, 50, 100, 60)


pen.hideturtle()


turtle.done()