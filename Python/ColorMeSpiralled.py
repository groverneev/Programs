import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "orange", "yellow",
          "green","blue", "purple", "pink", "gray", "sea green", "brown"]
your_name = turtle.textinput("Enter your name", "What is your name?")
sides = int(turtle.numinput("Number of sides",
                            "How many sides do you want (1-10)?", 10))
for x in range (1000):
    t.pencolor( colors[x%sides%10])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(your_name, font=("Arial", int( (x*2 + 4) / 4), "bold") )
    t.left(360/sides+2)