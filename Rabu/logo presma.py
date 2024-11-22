import turtle as t

t.speed(0)
t.bgcolor("white")
t.title("Logo SMK Prestasi Prima")

def draw_circle(color, radius, position):
    t.penup()
    t.goto(position)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def draw_square(color, size, position):
    t.penup()
    t.goto(position)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

def draw_rectangle(color, width, height, position, angle=0):
    t.penup()
    t.goto(position)
    t.setheading(angle) 
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

draw_circle("black", 160, (0, -160))

draw_circle("white", 140, (0, -140))

draw_circle("blue", 100, (0, -100))

draw_rectangle("red", 100, 40, (-50, -80)) 

thumb_angle = 30 
draw_rectangle("red", 23, 30, (-45, -20), angle=thumb_angle)  
draw_rectangle("red", 20, 90, (-35, -20))  
draw_rectangle("red", 20, 40, (-11, -20))  
draw_rectangle("red", 20, 33, (11, -20))  

draw_rectangle("red", 20, 33, (33, -20))  

t.penup()
t.goto(0, -200) 
t.color("black")
t.write("SMK PRESTASI PRIMA", align="center", font=("Arial", 20, "bold"))

t.penup()
t.goto(0, -230) 
t.color("black")
t.write("IF BETTER IS POSSIBLE, GOOD IS NOT ENOUGH", align="center", font=("Arial", 14, "italic"))

t.hideturtle()
t.done()