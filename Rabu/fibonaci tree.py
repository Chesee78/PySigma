import turtle

def draw_fibonacci_tree(t, branch_length, angle, depth):
    """Draw a Fibonacci tree with turtle t, branch length, angle, and depth."""
    if depth == 0:
        return

    t.forward(branch_length)
    t.left(angle)
    draw_fibonacci_tree(t, branch_length * 0.6, angle, depth - 1)
    t.right(2 * angle)
    draw_fibonacci_tree(t, branch_length * 0.6, angle, depth - 1)
    t.left(angle)
    t.backward(branch_length)

screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.pensize(2)
pen.color("green")
pen.speed(10)


pen.left(90)
pen.penup()
pen.goto(0, -250)
pen.pendown()

draw_fibonacci_tree(pen, 100, 30, 6)

pen.hideturtle()


turtle.done()