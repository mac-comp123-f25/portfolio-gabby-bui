import turtle

def spiral_in(turt, side_len):
    if side_len <= 5:
        while True:
            turt.speed(100)
            turt.right(10)
    else:
        turt.speed(100)
        turt.forward(side_len)
        turt.right(90)
        spiral_in(turt, side_len-5)

if __name__ == '__main__':
    window = turtle.Screen()
    spiral_in(turtle, 500)
    window.exitonclick()
