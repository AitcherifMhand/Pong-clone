import turtle
from ball import ball  
from paddle import paddle
game_Window=turtle.Screen()
game_Window.bgcolor('black')
game_Window.setup(width = 900, height = 750)
game_Window.tracer(0)


score = 0

def paddle_up():
    y = paddle.ycor()
    if y < 290:  
        y += 20
    paddle.sety(y)

def paddle_down():
    y = paddle.ycor()
    if y > -290:  
        y -= 20
    paddle.sety(y)

game_Window.listen()
game_Window.onkey(paddle_up, "Up")
game_Window.onkey(paddle_down, "Down")

game_over_text = turtle.Turtle()
game_over_text.speed(0)
game_over_text.color("white")
game_over_text.penup()
game_over_text.hideturtle()
game_over_text.goto(0, 260)
game_over_text.write("Score: 0", align="center", font=("Courier", 24, "normal"))


while True:
    game_Window.update()  

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 350:
        ball.sety(350)
        ball.dy *= -1 
    if ball.ycor() < -350:
        ball.sety(-350)
        ball.dy *= -1  
    if ball.xcor() > 400:
        ball.goto(0, 0)
        ball.dx *= -1  
        score = 0  
        game_over_text.clear()
        game_over_text.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -400:
        ball.goto(0, 0)
        ball.dx *= -1  
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle.ycor() + 50 and ball.ycor() > paddle.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1  
        score += 1  
        game_over_text.clear()
        game_over_text.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
