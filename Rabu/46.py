import turtle
from PIL import Image

def save_as_jpg(canvas, indonesiaflag):
    canvas.postscript(file = "indonesiaflag.eps")
    img = Image.open("indonesiaflag.eps")
    img.save("indonesiaflag.jpg")

def drawRectangle(ttl, x, y, width, height):
    """ Draw a rectangle of dimensions width and height, with upper left corner at (x, y). """
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    for i in range(2):
        ttl.forward(width)
        ttl.right(90)
        ttl.forward(height)
        ttl.right(90)
    ttl.penup()

def fillRectangle(ttl, x, y, width, height, color):
    ttl.fillcolor(color)
    ttl.begin_fill()
    drawRectangle(ttl, x, y, width, height)
    ttl.end_fill()

turtle.setup(1500, 1000, 0, 0)
screen = turtle.Screen()
screen.bgcolor("white")


myRed = "#D12421"
myWhite = "#FFFFFF"

Joe = turtle.Turtle()
Joe.screen.colormode(255)


width = 600
height = 300


fillRectangle(Joe, 0, 150, width, height / 2, myRed)


fillRectangle(Joe, 0, 0, width, height / 2, myWhite)

Joe.hideturtle()


ts = turtle.getscreen()
tc = ts.getcanvas()

tc.postscript(file="indonesiaflag.eps")
save_as_jpg(tc, "indonesiaflag")

turtle.done()