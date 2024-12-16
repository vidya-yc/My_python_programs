import turtle as Turtle
import time
print(Turtle.color("green"))
for angle in range(0,360,5):
    print(Turtle.seth(angle))
    print(Turtle.circle(100))
