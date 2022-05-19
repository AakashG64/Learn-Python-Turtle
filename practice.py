import turtle

t = turtle.Turtle()
screen = turtle.Screen()

screen.title("Practice Demo")
screen.bgcolor("black")
t.speed(0)
t.shape("turtle")

colors = ["red", "green", "blue", "white", "yellow", "pink"]
for i in range(30):
    t.color(colors[i%6])
    t.circle((i+1)*5)
    t.left(90)
    t.circle(-(i+1)*5)
    # t.circle((i+1)*2, 90, steps=4)

t.hideturtle()

turtle.done()