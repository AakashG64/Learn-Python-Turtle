import turtle

t = turtle.Turtle()
screen = turtle.Screen()

screen.title("Fractal Tree By Aakash Garg")
screen.bgcolor("black")
t.color("green")
t.shape("turtle")
t.pensize(2)

t.up()
t.goto(0, -250)
t.down()
t.left(90)
t.forward(100)
t.speed(10)

t.color("brown")
def tree(i):
    if i<10:
        return
    else:
        # t.color("brown")
        t.forward(i)
        t.color("orange")
        t.circle(2)
        t.color("red")
        t.left(30)
        tree(3*i/4)
        t.right(60)
        tree(3*i/4)
        t.left(30)
        t.backward(i)


tree(100)

t.hideturtle()

turtle.done()