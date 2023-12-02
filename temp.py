from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0) #(J.H) This initializes a vector that will represent the location of the food blocks on the game screen/
snake = [vector(10, 0)] #(J.H) This declares a list called snake with initially a single element which is a vector that starts at x coordinate 10, as the game continues to run, and the snake continues to grow the snake list will have more elements representing the snake body.
aim = vector(0, -10) #(J.H) The vector(x,y) function creates a vector that has mutable x and y values. For aim specifically, it changes the direction of the snake movement.
delay = 100 #(J.H) This variable declaration starts the beginning value of 100 miliseconds for whenever the game loop is called once again to increase the speed of the snake
score = 0 #(J.H) This variable delcaration starts the beginning value of ther player's score to zero

score_display = Turtle() #(J.H) The Turtle() function is the main function of the Turtle module. The Turtle() creates a screen that will draw onto an existing game window.
score_display.hideturtle() #(J.H) This is a function of the turtle module that hides the cursor of the Turtle() function whenever it draws something.
score_display.penup() #(J.H) This penup() function tells the score_display Turtle() to not draw when it moves from the centre of the game window when the game starts
score_display.goto(160, 180) #(J.H) This goto() function moves the text to the (x,y) coordinate of (160,180), the penup() function ensures that no line is drawn when the text is moved to the (160,190) coordinates
score_display.write(f"Score: {score}", align="center", font=("Arial", 14, "normal")) #(J.H) This write() function provides the actual letters/words we see on the screen. The first argument is what's being outputted onto the screen and because the score is being updated we use python f-string that allows us to embed changing values into our text, which in this case is the score. The other arguments configure the allignment, font, and size of the text. 

end_display = Turtle() #(J.H) We've previously discussed the reason for this function
end_display.hideturtle() #(J.H) We've previously discussed the reason for this function
end_display.penup() #(J.H) We've previously discussed the reason for this function

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

setup(420, 420, None, None) #(J.H) A function of the turtle module that sets up the game window width to 420 pixels, height to 420 pixels, and centres the window on the screen of a computer
title("Group 40 Snake Game") #(J.H) A function of the turtle module that changes the title of the game window from 'Python Turtle Graphics' to 'Group 40 Snake Game'
hideturtle() #(J.H) This is a function of the turtle module that hides the cursor of the Turtle() function that draws the food and red icon when the snake collides with it's own body. This removes the cursor head that appears if this was isvisible()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'd')
onkey(lambda: change(-10, 0), 'a')
onkey(lambda: change(0, 10), 'w')
onkey(lambda: change(0, -10), 's')
move() #(J.H) This calls the main game loop to run the game when the file is ran
done()