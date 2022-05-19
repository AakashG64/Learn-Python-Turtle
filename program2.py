import turtle

t = turtle.Turtle()
screen = turtle.Screen()

t.speed(6)
t.shape("turtle")
t.color("white")

screen.title("Draw Shapes")
screen.bgcolor("black")

# Square
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.fillcolor("red")
t.end_fill()

# Circle
t.begin_fill()
t.circle(20)            # +ve defines anti-clockwise
t.circle(-50)           # -ve means clockwise
# t.reset()
t.circle(100, 180)
t.fillcolor("yellow")
t.circle(100, 180, steps=9)
t.end_fill()
t.undo()

t.up()
t.goto(-200, 0)
t.down()
t.circle(40)
t.circle(-80)


t.hideturtle()

turtle.done()