import turtle

def tele_turtle(n):
    win = turtle.Screen()
    tele_t = turtle.Turtle()
    for i in range(n):
        move = input("Enter net move: ")
        do_move(tele_t,move)
    win.exitonclick()

def do_move(tele_t, move):
    if move == "f":
        tele_t.forward(15)
    elif move == "b":
        tele_t.back(15)
    elif move == "r":
        tele_t.right(90)
    elif move == "1":
        tele_t.left(90)
    else:
        print("Invalid move")

if __name__ == "__main__":
    tele_turtle(10)
