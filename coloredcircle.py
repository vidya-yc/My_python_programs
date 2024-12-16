import turtle as Turtle
print(Turtle.speed(0))
print(Turtle.bgcolor("Black"))

colors = ['Red','Yellow','Cyan','Orange','pink','Purple']

for x in range(100):
    print(Turtle.circle(x))
    print(Turtle.color(colors[x%6]))
    print(Turtle.left(60))

Turtle.bye()