import turtle
import math

win = turtle.Screen()
win.bgcolor("light sky blue")

sepalTurtle = turtle.Turtle()
sepalTurtle.speed(0)
sepalTurtle.color("dark green", "spring green")
sepalTurtle.hideturtle()

petalTurtle = turtle.Turtle()
petalTurtle.speed(0)
petalTurtle.color('dark red', 'light coral')
petalTurtle.hideturtle()

centerTurtle = turtle.Turtle()
centerTurtle.speed(0)
centerTurtle.color('purple4')
centerTurtle.hideturtle()

stampTurtle = turtle.Turtle()
stampTurtle.color("gold")
stampTurtle.speed(0)
stampTurtle.shape("turtle")
stampTurtle.hideturtle()

def drawFlower(turt1, turt2, turt3, turt4, centerX, centerY):
    centerY_equation = int(centerY - 15)
    centerX_equation = int(centerX - 2)
    drawFiveCircles(turt1, 50, centerX, centerY)
    drawFiveCircles(turt2, 25, centerX, centerY)
    drawCenterCircle(turt3, centerX, centerY_equation)
    drawBee(turt4, centerX_equation, 0)

def drawFiveCircles(turt, radius, centerX, centerY):
    turt.up()
    turt.goto(centerX, centerY)
    turt.down()
    for i in range(5):  # Changed into loop function
        turt.begin_fill()
        turt.circle(radius)
        turt.end_fill()
        turt.left(72)

def drawCenterCircle(turt, centerX, centerY):
    turt.up()
    turt.goto(centerX, centerY)
    turt.down()
    turt.begin_fill()
    turt.circle(15)
    turt.end_fill()

def drawBee(turt, centerX, centerY):
    turt.up()
    turt.goto(centerX, centerY)
    turt.down()
    turt.stamp()

"""
This function is to draw all 5 flowers at the same time
"""
def drawAll():
    drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 0, 0)
    drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 0, 220)  # check
    drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 220, 0)
    drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 0, -220)  # check
    drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, -220, 0)

    win.exitonclick()

drawAll()
