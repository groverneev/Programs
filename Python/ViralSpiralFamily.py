import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "orange", "yellow",
          "green","blue", "purple", "pink", "gray", "sea green", "brown"]
family = []
name = turtle.textinput("My family",
                        "Enter a name, or just hit [ENTER] to end:")
while name != "":
    family.append(name)
    name = turtle.textinput("My family",
                        "Enter a name, or just hit [ENTER] to end:")
for m in range(100):
    t.forward(m*4)
    position = t.position()
    heading = t.heading()
    for n in range(len(family)):
        t.pendown()
        t.pencolor(colors[n%len(family)%10])
        t.write(family[n%len(family)], font = ("Arial", int((m+4)/4), "bold") )
        t.right(360/len(family))
        t.penup()
        t.forward(m//2)
    t.setposition(position)
    t.setheading(heading)
    t.left(360/len(family) + 3)
