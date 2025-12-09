import turtle
import math

def drawFiveCircles(turt,radius,centerX,centerY):
    turt.up()  # TODO: Step 2: start here
    turt.goto(centerX,centerY)
    turt.down()
    for i in range(5):  # Changed into loop function
        turt.begin_fill()
        turt.circle(radius)
        turt.end_fill()
        turt.left(72)

def drawCenterCircle(turt,centerX,centerY):
    turt.up()
    turt.goto(centerX,centerY)
    turt.down()
    turt.begin_fill()
    turt.circle(15)
    turt.end_fill()


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

drawFiveCircles(sepalTurtle,50,0,0)
drawFiveCircles(petalTurtle,25,0,0)

drawCenterCircle(centerTurtle,0,-15)

stampTurtle.up()
stampTurtle.goto(-2,0)
stampTurtle.down()
stampTurtle.stamp()

drawFiveCircles(sepalTurtle,50,0,220)
drawFiveCircles(petalTurtle,25,0,220)

drawCenterCircle(centerTurtle,0,205)

stampTurtle.up()
stampTurtle.goto(-2,220)
stampTurtle.down()
stampTurtle.stamp()

drawFiveCircles(sepalTurtle,50,220,0)
drawFiveCircles(petalTurtle,25,220,0)

drawCenterCircle(centerTurtle,220,-15)

stampTurtle.up()
stampTurtle.goto(218,0)
stampTurtle.down()
stampTurtle.stamp()

drawFiveCircles(sepalTurtle,50,0,-220)
drawFiveCircles(petalTurtle,25,0,-220)

drawCenterCircle(centerTurtle,0,-235)

stampTurtle.up()
stampTurtle.goto(-2,-220)
stampTurtle.down()
stampTurtle.stamp()

drawFiveCircles(sepalTurtle,50,-220,0)
drawFiveCircles(petalTurtle,25,-220,0)

drawCenterCircle(centerTurtle,-220,-15)

stampTurtle.up()
stampTurtle.goto(-222,0)
stampTurtle.down()
stampTurtle.stamp()

win.exitonclick()