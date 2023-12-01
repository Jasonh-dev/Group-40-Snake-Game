from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
delay = 100
score = 0

score_display = Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(160, 190)
score_display.write(f"Score: {score}", align="center", font=("Arial", 14, "normal"))
end_display = Turtle()
end_display.hideturtle()
end_display.penup()

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def move():
    """Move snake forward one segment."""
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
    
    if head in snake:
        square(head.x, head.y, 9, 'red')
        end_display.write(f"You Lose!", align="center", font=("Arial", 14, "normal"))
        update()
        return

    snake.append(head)

    if head == food:
        score +=1
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Arial", 14, "normal"))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        delay -= 5
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, delay)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'd')
onkey(lambda: change(-10, 0), 'a')
onkey(lambda: change(0, 10), 'w')
onkey(lambda: change(0, -10), 's')
move()
done()