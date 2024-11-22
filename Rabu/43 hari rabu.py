import turtle

screen = turtle.Screen()
screen.bgcolor("purple")

pen = turtle.Turtle()
pen.speed(0)

pen.fillcolor("blue")
pen.begin_fill()

pen.circle(50)

pen.end_fill()
pen.hideturtle()

pen.fillcolor("blue")
pen.begin_fill()

pen.circle(150)

pen.end_fill()
pen.hideturtle()

turtle.done()