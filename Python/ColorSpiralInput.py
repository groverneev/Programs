import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "orange", "yellow", "green","blue", "purple", "pink", "gray"]
sides = int( turtle.numinput("Number of sides",
                             "How many sides do you want (1-8)?", 4, 1, 8))
for x in range (1000):
    t.pencolor( colors[ x % sides] )
    t.forward( x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides / 200)
