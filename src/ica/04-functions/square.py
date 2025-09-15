import turtle

def turtle_square(sqTurt,side_len):
    for i in range(4):
        sqTurt.forward(side_len)
        sqTurt.left(90)

window = turtle.Screen()
Dobby = turtle.Turtle()
turtle_square(Dobby,100)
window.exitonclick()


