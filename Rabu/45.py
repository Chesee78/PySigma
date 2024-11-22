import turtle

screen = turtle.Screen()
screen.bgcolor('yellow')

tt = turtle.Turtle()
tt.pensize(2)

for i in range(6):
    for color in ('red', 'magenta', 'blue', 'cyan', 'green', 'white', 'yellow'):
        tt.color(color)
        tt.circle(100)
        tt.circle(10)

tt.hideturtle()

turtle.done()