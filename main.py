import turtle
import time
import game


STAMP_SIZE = 20


game = game.Game()

screen = turtle.Screen()
screen.title('Pong')
screen.bgcolor('black')
screen.setup(game.width, game.height)
screen.tracer(0)
screen.cv._rootwindow.resizable(False, False)

ball = turtle.Turtle()
ball.shape('circle')
ball.color('red')
ball.penup()

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(game.paddle_height / STAMP_SIZE, game.paddle_width / STAMP_SIZE)
paddle_a.penup()

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(game.paddle_height / STAMP_SIZE, game.paddle_width / STAMP_SIZE)
paddle_b.penup()


# Text
text = turtle.Turtle()
text.goto(0, game.height / 2 - 50)
text.color('white')
text.penup()
text.write(f'Player A: 0, Player B: 0', align='center', font=('Courier', 20, 'normal'))
text.hideturtle()

# Listen to keyboard events
def player_a_up():
    game.paddle_a_up()


def player_a_down():
    game.paddle_a_down()


def player_b_up():
    game.paddle_b_up()


def player_b_down():
    game.paddle_b_down()


screen.listen()
screen.onkeypress(player_a_up, 'w')
screen.onkeypress(player_a_down, 's')
screen.onkeypress(player_b_up, 'Up')
screen.onkeypress(player_b_down, 'Down')

previous_points_a = None
previous_points_b = None

finished = turtle.Turtle()
finished.hideturtle()
already_finished = False

while True:

    game.tick()
    ball.goto(game.ball_pos())
    paddle_a.goto(game.paddle_a_pos)
    paddle_b.goto(game.paddle_b_pos)

    if previous_points_a != game.points_a or previous_points_b != game.points_b:
        text.clear()
        text.write(f'Player A: {game.points_a}, Player B: {game.points_b}', align='center', font=('Courier', 20, 'normal'))
        previous_points_a = game.points_a
        previous_points_b = game.points_b

    if game.game_over and not already_finished:
        finished.clear()
        finished.write('Game Over', align='center', font=('Courier', 45, 'normal'))
        already_finished = True

    screen.update()
    time.sleep(0.00000004)
