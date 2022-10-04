import turtle
def phaluss():
    turtle.color("purple","white")
    turtle.width(6)
    turtle.penup()
    turtle.speed(20)
    x = 1
    while x == 1:
        turtle.left(8)
        turtle.goto(-59,-21)
        turtle.pendown()
        z = 0
        c = 1
        while c ==1:
            turtle.right(4.5)
            turtle.forward(3)
            z = z+1
            if z == 90:
                break
        turtle.penup()
        turtle.left(76)
        turtle.goto(-5,-28)
        turtle.pendown()
        z = 0
        c = 1
        while c ==1:
            turtle.right(4.5)
            turtle.forward(3)
            z = z+1
            if z == 90:
                break
        turtle.penup()
        turtle.left(97)
        turtle.goto(-58,-20)
        turtle.pendown()
        turtle.goto(-58,150)
        z = 0
        c = 1
        while c ==1:
            turtle.right(4.5)
            turtle.forward(3)
            z = z+1
            if z == 40:
                break
        turtle.goto(18,-20)
        turtle.penup()
        turtle.goto(18,135)
        turtle.pendown()
        turtle.goto(-58,135)
        turtle.penup()
        turtle.goto(-20,187)
        turtle.pendown()
        turtle.goto(-20,165)
        turtle.penup()
        turtle.goto(-20,187)
        turtle.left(180)
        turtle.penup()
        turtle.goto(9999,9999)
        break
