import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
sides = 7
colors = ["red", "orange", "yellow", "green", "blue","purple", "pink"]
for x in range (1000):
    t.pencolor(colors[x%sides])
    t.forward(x * 3 / sides)
    t.left(360/sides + 1)
    t.width(x*sides/100)
