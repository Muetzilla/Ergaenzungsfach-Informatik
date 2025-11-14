import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

turtle.tracer(0)

ANGLE = 60

def draw(size):
    if size < 1:
        return
    else:
        t.fd(size)
        t.left(ANGLE)
        draw(size * 0.5)
        t.right(2 * ANGLE)
        draw(size * 0.5)
        t.left(ANGLE)
        t.fd(size)
        draw(size * 0.5)
        t.backward(2 * size)

t.penup()
t.goto(0, -0)
t.pendown()

for i in range(36):
    draw(100)
    t.left(10)

turtle.update()

turtle.done()
