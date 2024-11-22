import turtle
import time
import random

print("This program draws shapes based on the number you enter in a uniform pattern.")
num_str = input("Enter the side number of the shape you want to draw: ")
if num_str.isdigit():
    squares = int(num_str)

    angle = 180 - 180 * (squares - 2) / squares

    turtle.up()

    x = 0
    y = 0
    turtle.setpos(x, y)

    numshapes = 8
    for _ in range(numshapes):
        turtle.color(random.random(), random.random(), random.random())
        x += 5
        y += 5
        turtle.forward(x)
        turtle.left(y)
        turtle.begin_fill()
        turtle.down()
        for _ in range(squares):
            turtle.forward(40)
            turtle.left(angle)
        turtle.end_fill()
        turtle.up()

    print(turtle.pos())
    time.sleep(11)
    turtle.bye()
else:
    print("Please enter a valid number.")