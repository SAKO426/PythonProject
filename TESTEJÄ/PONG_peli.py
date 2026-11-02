import turtle

# Ikkuna
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=1500, height=1000)
wn.tracer(0)

# Pelaaja A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Pelaaja B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Pallo
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = 0.1
ball.dy = 0.1

# Mailojen liike
def paddle_a_up():
    y = paddle_a.ycor()
    paddle_a.sety(y + 20)

def paddle_a_down():
    y = paddle_a.ycor()
    paddle_a.sety(y - 20)

def paddle_b_up():
    y = paddle_b.ycor()
    paddle_b.sety(y + 20)

def paddle_b_down():
    y = paddle_b.ycor()
    paddle_b.sety(y - 20)

# Näppäimet
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Pelisilmukka
while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ylä- ja alareuna
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Vasen ja oikea reuna
    if ball.xcor() > 390:
        ball.goto(0, 0)

    if ball.xcor() < -390:
        ball.goto(0, 0)

    # Maila B
    if (340 < ball.xcor() < 350 and
            paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    # Maila A
    if (-350 < ball.xcor() < -340 and
            paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1