import turtle

t = turtle.Turtle()
screen = turtle.Screen()
print(screen.window_width(),screen.window_height(),sep="\n")
# Screen Size ------------------- 768 width and 648 height
# Constraints
t.speed(6)
t.shape("turtle")
t.color("white")
screen.title("Shapes By Aakash")
screen.bgcolor("black")

# Drawing Shapes
# Vertical Line
t.up()
t.goto(0, -324)
t.down()
t.left(90)
t.forward(648)
# Horizontal Line
t.up()
t.goto(-384, 0)
t.down()
t.right(90)
t.forward(768)

# Rectangle
t.up()
t.goto(-250, -200)
t.down()
t.color("blue")
for i in range(2):
    t.forward(150)
    t.left(90)
    t.forward(80)
    t.left(90)
t.hideturtle()

# Circle
t.up()
t.goto(200, 100)
t.down()
t.color("red")
t.circle(80)
t.hideturtle()

# Square
t.up()
t.goto(150, -200)
t.down()
t.color("yellow")
for i in range(4):
    t.forward(100)
    t.left(90)
t.hideturtle()

# Polygons
t.up()
t.goto(-200, 100)
t.down()
t.color("white")
t.circle(80, steps=12)
t.hideturtle()

turtle.done()