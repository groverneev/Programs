import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "orange", "yellow",
          "green","blue", "purple", "pink", "gray", "sea green", "brown"]
family = []
name = turtle.textinput("My family",
                        "Enter up to 10 names, or just hit enter to end.")
while name != "":
    family.append(name)
    name = turtle.textinput("My family",
                        "Enter up to 10 names, or just hit enter to end.")
for x in range (100):
    t.pencolor(colors[x%len(family)])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(family[x%len(family)], font = ("Arial", int((x+4)/4), "bold") )
    t.left(360/len(family) + 2)
