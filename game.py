import turtle
import ball.py as Ball
import paddle.py as player
game_Window=turtle.screen()
game_Window.bgcolor('black')
game_Window.setup(width = 900, height = 750)
game_Window.tracer(0)


#Main loop

while True :
    game_Window.update()