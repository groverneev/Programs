import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "orange", "yellow", "green","blue"]
your_name = turtle.textinput("Enter your name", "What is your name?")
for x in range (100):
    t.pencolor( colors[ x % 5] )
    t.penup()
    t.forward( x * 4 )
    t.pendown()
    t.write(your_name, font = ("Arial", int( (x + 4) / 4), "bold") )
    t.left(92)
