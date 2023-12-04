#One Player Snake Game All Functions & Game Code

from random import randrange
from turtle import *
from freegames import square, vector

# Initialize game variables
food = vector(0, 0) 
delay = 100
end_display = Turtle()

# Initializes variables for Snake 1/Player 1
snake = [vector(10, 0)]
aim = vector(0, -10)
score = 0

# Initializes the size of the game window and background colour to black
setup(450, 450, None, None)
bgcolor('black')
hideturtle()

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
score_display.goto(0, 200)
score_display.color('yellow')
score_display.write(f"P1 Score: {score}", align="center", font=("Arial", 14, "normal"))

restart_display = Turtle()
restart_display.hideturtle()
restart_display.penup()
restart_display.goto(0,-25)

#Creates the game ending acknowledgement
def lose_display():
    end_display.hideturtle()
    end_display.penup()
    
def change(x, y):
    aim.x = x
    aim.y = y

def restart_game():
    global delay, score, aim, snake
    delay = 100
    score = 0
    aim = vector(0,-10)
    snake = [vector(10,0)]
    
    score_display.clear()
    score_display.write(f"P1 Score: {score}", align="center", font=("Arial", 14, "normal"))
    
    end_display.clear()
    end_display.hideturtle()
    
    restart_display.clear()
    
    
    one_player()

def one_player():
    
    head = snake[-1].copy()
    head.move(aim)
    
    global delay
    global score
    
    if head.x >= 200:
        head.x = -200
    elif head.x < -200:
        head.x = 190
        
    if head.y >= 200:
        head.y = -200
    elif head.y < -200:
        head.y = 190
    
    lose_display()
    
    if head in snake:
        square(head.x, head.y, 9, 'red')
        end_display.color('yellow')
        end_display.write("Player 1 Loses! Restarting in 6 seconds...", align="center", font=("Arial", 14, "normal"))
        restart_display.color('yellow')
        restart_display.write(f"Click on the screen at any times to end the game", align="center", font=("Arial", 14, "normal"))
        ontimer(restart_game,6000)
        exitonclick()
        return
    
    snake.append(head)
    
    if head == food:
        score += 1
        score_display.clear()
        score_display.write(f"P1 Score: {score}", align="center", font=("Arial", 14, "normal"))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        delay -= 5
    else:
        snake.pop(0)
        
        clear()

    for body in snake:
        square(body.x, body.y, 9, 'yellow')
    
    square(food.x, food.y, 9, 'green')
    update()
    ontimer(one_player, delay)

tracer(False)
listen()
onkey(lambda: change(10, 0), 'd')
onkey(lambda: change(-10, 0), 'a')
onkey(lambda: change(0, 10), 'w')
onkey(lambda: change(0, -10), 's')
one_player()
done()