import turtle

def drawPentagon(ttl, x, y, side_length, color):
    """Draw a pentagon with the starting point at (x, y) and sides of side_length and given color."""
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    ttl.fillcolor(color)
    ttl.begin_fill()
    for _ in range(5):
        ttl.forward(side_length)
        ttl.left(72) 
    ttl.end_fill()
    ttl.penup()


screen = turtle.Screen()
screen.bgcolor("white")


pen = turtle.Turtle()
pen.pensize(2)
pen.color("purple")

drawPentagon(pen, 0, 0, 100, "purple")


pen.hideturtle()


turtle.done()