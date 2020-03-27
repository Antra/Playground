import turtle


def tree(branchLen, t):
    if branchLen < 20:
        t.color("brown")
        t.pensize(2)
    else:
        t.color("green")
        t.pensize(3)
    if branchLen > 5:
        t.down()
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15, t)
        t.left(40)
        tree(branchLen-15, t)
        t.right(20)
        t.up()
        t.backward(branchLen)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    t.pensize(10)
    tree(75, t)
    myWin.exitonclick()


main()
