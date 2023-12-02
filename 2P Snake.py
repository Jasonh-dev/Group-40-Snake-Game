from random import randrange
from turtle import *

from freegames import square, vector

# Initialize game variables for the first snake
food = vector(0, 0)
snake1 = [vector(10, 0)]
aim1 = vector(0, -10)
delay = 100
score1 = 0

# Initialize game variables for the second snake
snake2 = [vector(-10, 0)]
aim2 = vector(0, 10)
score2 = 0

setup(450, 450, None, None)
bgcolor('black')

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

score_display2 = Turtle()
score_display2.hideturtle()
score_display2.penup()
score_display2.goto(70,200)
score_display2.color('cyan')
score_display2.write(f"P2 Score: {score2}", align="center", font=("Arial", 14, "normal"))

score_display = Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-70, 200)
score_display.color('yellow')
score_display.write(f"P1 Score: {score1}", align="center", font=("Arial", 14, "normal"))

end_display = Turtle()
end_display.hideturtle()
end_display.penup()

def change1(x, y):
    aim1.x = x
    aim1.y = y

def change2(x, y):
    aim2.x = x
    aim2.y = y

def move():
    head1 = snake1[-1].copy()
    head1.move(aim1)

    head2 = snake2[-1].copy()
    head2.move(aim2)

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
    
    if head1 in snake1:
        square(head1.x, head1.y, 9, 'red')
        end_display.color('yellow')
        end_display.write(f"Player 1 Loses!", align="center", font=("Arial", 14, "normal"))
        update()
        return
    elif head1 in snake2:
        square(head1.x, head1.y, 9, 'red')
        end_display.color('yellow')
        end_display.write(f"Player 1 Loses!", align="center", font=("Arial", 14, "normal"))
        update()
        return
    elif head2 in snake2:
        square(head2.x, head2.y, 9, 'red')
        end_display.color('cyan')
        end_display.write(f"Player 2 Loses!", align="center", font=("Arial", 14, "normal"))
        update()
        return
    elif head2 in snake1:
        square(head2.x, head2.y, 9, 'red')
        end_display.color('cyan')
        end_display.write(f"Player 2 Loses!", align="center", font=("Arial", 14, "normal"))
        update()
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
    ontimer(move, delay)

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

move()
done()
