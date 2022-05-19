import turtle

t = turtle.Turtle()
screen = turtle.Screen()

print(t.shape(),t.color(),sep="\n")

t.speed(0)
t.shape("turtle")
t.color("red", "green")

# turtle.colormode(255)
# t.color(100,200,155)

# Screen Methods
screen.bgcolor("black")
screen.title("Aakash Graphics")
# screen.bgpic("C:\\Users\\Aakash Garg\\PycharmProjects\\Learn Turtle\\assets\\img_1.gif")

# Square
colors = ["red", "white", "green", "blue", "yellow", "pink"]
for i in range(100):
    t.color(colors[i%6])
    t.forward((i+1)*5)
    t.left(90)

t.hideturtle()

turtle.done()