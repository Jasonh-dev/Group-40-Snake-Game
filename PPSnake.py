#Two Player Snake Game All Functions & Game Code

from random import randrange
from turtle import *

from freegames import square, vector

# Initialize game variables
food = vector(0, 0)
delay = 100
end_display = Turtle()

# Initializes variables for Snake 1/Player 1
snake1 = [vector(10, 0)]
snake1_aim1 = vector(0, -10)
score1 = 0

# Initializes variables for the Snake 2/Player 2
snake2 = [vector(-10, 0)]
snake2_aim2 = vector(0, 10)
score2 = 0

# Initializes the size of the game window and background colour to black
setup(450, 450, None, None)
bgcolor('black')

#Creates the border of the game
border = Turtle()
border.hideturtle()
border.penup()
border.goto(200,200)
border.color('magenta')
border.pendown()
border.goto(-200,200)
border.goto(-200,-200)
border.goto(200,-200)
border.goto(200,200)

#Creates the score display for Snake 1/Player 1
score_display = Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-70, 200)
score_display.color('yellow')
score_display.write(f"P1 Score: {score1}", align="center", font=("Arial", 14, "normal"))

#Creates the score display for Snake 2/Player 2
score_display2 = Turtle()
score_display2.hideturtle()
score_display2.penup()
score_display2.goto(70,200)
score_display2.color('cyan')
score_display2.write(f"P2 Score: {score2}", align="center", font=("Arial", 14, "normal"))

restart_display = Turtle()
restart_display.hideturtle()
restart_display.penup()
restart_display.goto(0,-25)

#Creates the game ending acknowledgement
def lose_display():
    end_display.hideturtle()
    end_display.penup()

def restart_game():
    global delay, score1, snake1, score2, snake2_aim2, snake2, snake1_aim1
    delay = 100
    
    score1 = 0
    snake1_aim1 = vector(0,-10)
    snake1 = [vector(10,0)]
    
    score2 = 0
    snake2_aim2 = vector(-10, 0)
    snake2 = [vector(-10,0)]
    
    score_display.clear()
    score_display.write(f"P1 Score: {score1}", align="center", font=("Arial", 14, "normal"))
    
    score_display2.clear()
    score_display2.write(f"P2 Score: {score2}", align="center", font=("Arial", 14, "normal"))
    
    end_display.clear()
    end_display.hideturtle()
    
    restart_display.clear()
    
    two_player()

def change1(x, y):
    snake1_aim1.x = x
    snake1_aim1.y = y

def change2(x, y):
    snake2_aim2.x = x
    snake2_aim2.y = y

def two_player():
    head1 = snake1[-1].copy()
    head1.move(snake1_aim1)

    head2 = snake2[-1].copy()
    head2.move(snake2_aim2)

    global delay
    global score1
    global score2

    if head1.x >= 200:
        head1.x = -200
    elif head1.x < -200:
        head1.x = 190
    if head1.y >= 200:
        head1.y = -200
    elif head1.y < -200:
        head1.y = 190
    
    if head2.x >= 200:
        head2.x = -200
    elif head2.x < -200:
        head2.x = 190
    if head2.y >= 200:
        head2.y = -200
    elif head2.y < -200:
        head2.y = 190
    
    lose_display()
    
    if head1 in snake1:
        square(head1.x, head1.y, 9, 'red')
        end_display.color('yellow')
        end_display.write(f"Player 1 Loses! Restarting in 6 seconds...", align="center", font=("Arial", 14, "normal"))
        restart_display.color('yellow')
        restart_display.write(f"Click on the screen at any time to end the game", align="center", font=("Arial", 14, "normal"))
        ontimer(restart_game,6000)
        exitonclick()
        return
    elif head1 in snake2:
        square(head1.x, head1.y, 9, 'red')
        end_display.color('yellow')
        end_display.write(f"Player 1 Loses! Restarting in 6 seconds...", align="center", font=("Arial", 14, "normal"))
        restart_display.color('yellow')
        restart_display.write(f"Click on the screen at any times to end the game", align="center", font=("Arial", 14, "normal"))
        ontimer(restart_game,6000)
        exitonclick()
        return
    elif head2 in snake2:
        square(head2.x, head2.y, 9, 'red')
        end_display.color('cyan')
        end_display.write(f"Player 2 Loses! Restarting in 6 seconds...", align="center", font=("Arial", 14, "normal"))
        restart_display.color('cyan')
        restart_display.write(f"Click on the screen at any times to end the game", align="center", font=("Arial", 14, "normal"))
        ontimer(restart_game,6000)
        exitonclick()
        return
    elif head2 in snake1:
        square(head2.x, head2.y, 9, 'red')
        end_display.color('cyan')
        end_display.write(f"Player 2 Loses! Restarting in 6 seconds...", align="center", font=("Arial", 14, "normal"))
        restart_display.color('cyan')
        restart_display.write(f"Click on the screen at any times to end the game", align="center", font=("Arial", 14, "normal"))
        ontimer(restart_game,6000)
        exitonclick()
        return

    snake1.append(head1)
    snake2.append(head2)

    if head1 == food:
        score1 += 1
        
        score_display.clear()
        score_display.write(f"P1 Score: {score1}", align="center", font=("Arial", 14, "normal"))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        delay -= 5
    else:
        snake1.pop(0)

    if head2 == food:
        score2 += 1
        score_display2.clear()
        score_display2.write(f"P2 Score: {score2}", align="center", font=("Arial", 14, "normal"))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        delay -= 5
    else:
        snake2.pop(0)

    clear()

    for body in snake1:
        square(body.x, body.y, 9, 'yellow')
    for body in snake2:
        square(body.x, body.y, 9, 'cyan')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(two_player, delay)

hideturtle()
tracer(False)
listen()

onkey(lambda: change1(10, 0), 'd')
onkey(lambda: change1(-10, 0), 'a')
onkey(lambda: change1(0, 10), 'w')
onkey(lambda: change1(0, -10), 's')

onkey(lambda: change2(10, 0), 'Right')
onkey(lambda: change2(-10, 0), 'Left')
onkey(lambda: change2(0, 10), 'Up')
onkey(lambda: change2(0, -10), 'Down')

two_player()
done()