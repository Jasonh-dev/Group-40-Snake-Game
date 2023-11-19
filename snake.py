"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries.""" 
#This function checks whether the given head position is inside the boundaries of the game screen. The game screen has a width and height of 400 units each, and the boundaries are defined as -200 to 190 for both the x and y coordinates. If the head is within these boundaries, the function returns True; otherwise, it returns False.

    return -200 < head.x < 190 and -200 < head.y < 190

#Move Functions
def move():
    """Move snake forward one segment.""" 
#This function is responsible for moving the snake 

#Copy Head Position:
    head = snake[-1].copy() 
#Creates a copy of the current head position.
    
#Move Head:
    head.move(aim)
#Moves the head in the direction specified by the aim vector. The aim vector determines the direction in which the snake is moving.

#Check for Collision:
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return 
#Checks if the head is outside the game boundaries or if it collides with the snake itself. If either condition is true, the game ends. The head position is marked with a red square, and the game is updated.

#Update Snake Length:
   snake.append(head) #Adds the new head position to the snake

#Check for Food Eaten:
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
#If the head coincides with the food position, the snake has eaten the food. The snake's length is printed, and a new position for the food is randomly generated. Otherwise, the snake's tail is popped, maintaining its length.

#Clear the Screen:
    clear()
#Clears the screen to update the display with the new snake and food positions.

#Draw Snake and Food:
    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
#Draws the snake segments in black and the food in green.

#Update Display:
    update()

#Game Loop:
    ontimer(move, 100)
#Uses the ontimer function to create a game loop, calling the move function every 100 milliseconds to continue the game.

#End of move functions

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()

