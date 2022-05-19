import turtle

t = turtle.Turtle()
screen = turtle.Screen()        #width: 768px and height: 648px

print((screen.window_width(),screen.window_height()))
screen.title("Satya By Aakash Garg")
screen.bgcolor("black")
t.speed(0)
t.color("yellow")
t.shape("turtle")

# Part1
t.up()
t.goto(-344, -284)
t.down()
t.left(240)
t.forward(30)
t.backward(30)
t.left(120)
t.forward(344)
t.left(90)
t.forward(568)
t.right(90)
t.forward(344)
t.left(60)
t.forward(30)

# Part2
t.up()
t.goto(-344, 284)
t.down()
t.left(90)
t.forward(30)
t.backward(30)
t.right(240)
t.forward(284)
t.left(90)
t.forward(688)
t.right(90)
t.forward(284)
t.left(60)
t.forward(30)

# Part3
goto = [(-192, -162), (-192, 132), (162, 132), (162, -162)]
for i in range(4):
    t.up()
    t.goto(goto[i])
    t.down()
    t.color("red")
    t.begin_fill()
    t.fillcolor("red")
    t.circle(20)
    t.end_fill()


t.hideturtle()

turtle.done()