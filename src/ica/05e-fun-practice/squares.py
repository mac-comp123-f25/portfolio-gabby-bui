import turtle

win = turtle.Screen()
gabby = turtle.Turtle()
gabby.goto(-200,-200)
gabby.speed(100)

def draw_nested_squares(turt):
    for i in range (10,500,10):
        for j in range (4):
            turt.forward(i)
            turt.left(90)

draw_nested_squares(gabby)
win.exitonclick()
