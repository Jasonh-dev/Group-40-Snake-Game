#Original Snake Code File/Game
#Jason Hui (J.H)

from random import randrange
#(J.H) The randrange function generates a random integer between a specified range (exclusive).
#(J.H) We use this function to generate the (x,y) coordinates of the food block once it has been eaten by a snake. 

from turtle import *
#(J.H) The turtle module is the basis for this entire game, as the module has all the functions that create the game window.
#(J.H) Additionally, the module has functions that aid in updating the game window as the user interacts with the game, and most importantly provides a function to exit the program.

from freegames import square, vector
#(J.H) The freegames module is a collection of pre-coded games and game functions that can be played and used, including the original snake game that we altered.
#(J.H) The square function takes in 4 arguments (x, y, size, name) and it draws a square at the (x,y) coordinate with the specified side length (size) and the 'name' of the colour to fill in the square
#(J.H) We use the square function to draw the squares to represent the head & body of the snake as well as the food blocks.
#(J.H) 'vector' is a class that defines a two dimensional vector with its own methods.
#(J.H) We use the vector(x,y) function to create two dimensional vectors to represent our snake's initial direction and the snake's aim function which enables the user to change the snake's direction. As well, we create the initial coordinates for the food blocks.

#(J.H) Intializing game variables
food = vector(0, 0) #(J.H) Using the vector() function we create a 2d vector to repesent coordinates to spawn food blocks, which we make the first block to spawn at the centre of the game screen.
snake = [vector(10, 0)] #(J.H) We assign a list with initially one 2d vector to represent the initial position of the snake to a variable name called snake. The snake list will be added with more vectors representing the body of the snake as it continues to eat food.
aim = vector(0, -10) #(J.H) Using the vector() function we create a 2d vector to initialize the first movement of the snake which is in a downward motion.


def change(x, y): #(J.H) This function changes the (x,y) value of the vector that changes the snake's movement
    """Change snake direction."""
    aim.x = x #(J.H) The vector.x() function changes the x-value of the two dimensional vector. We use this function to state that the x value in the vector defined by aim is equal to the first argument of the change function, which will be used/changed in the controls of the player at the bottom of the code.
    aim.y = y #(J.H) The vector.y() function changes the y-value of the two dimensional vector. We use this function to state that the y value in the vector defined by aim is equal to the second argument of the change function, which will be used/changed in the controls of the player at the bottom of the code.


def inside(head): #This function checks whether the given head position is inside the boundaries of the game screen
    """Return True if head inside boundaries.""" 
    return -200 < head.x < 190 and -200 < head.y < 190 
    #The boundaries are defined as -200 to 190 for both the x and y coordniates
    #When the head is between this boundaries, the function returns true, otherwise False

def move(): #This function is responsible for moving the snake 
    """Move snake forward one segment.""" 

    head = snake[-1].copy() #Creates a copy of the current head position
    
    head.move(aim) #Moves the head in the direction specified by the aim vector. The aim vector determines the direction in which the snake is moving.

#Check for Collision:
    if not inside(head) or head in snake: #Checks if the head is outside the game boundaries or if it collides with the snake itself. If either condition is true, the game ends. The head position is marked with a red square, and the game is updated.
        square(head.x, head.y, 9, 'red') #(J.H) We use the square() function to draw a red sqaure with a side length of 9 at the (x,y) coordinate of the head.
        update()
        return 

#Update Snake Length:
    snake.append(head) #Adds the new head position to the snake

#Check for Food Eaten:
    if head == food: #If the head (x,y) coordinates coincides with the food position, the snake has eaten the food. The snake's length is printed, and a new position for the food is randomly generated. 
        print('Snake:', len(snake)) #(J.H) The length of the snake is printed in the terminal that is running the game
        food.x = randrange(-15, 15) * 10 #(J.H) Once the food has been eaten, we use the randrange() function to generate a new x-coordinate to spawn the food block.
        food.y = randrange(-15, 15) * 10 #(J.H) Once the food has been eaten, we use the randrange() function to generate a new y-coordinate to spawn the food block.
    else:
        snake.pop(0) #(J.H) If the snake have not eaten the food, then we remove the first element (index 0) within the snake list using the pop() function which is a method of a list. The pop() function returns and removes the element at the index value indicated by the argument within a list.



    clear() #Clears the screen to update the display with the new snake and food positions.

#Draw Snake and Food:
    for body in snake: #(J.H) The use of the for loop walks through the snake list and uses the (x,y) coordinate of the vectors to use the square() function to draw the body as a black square with a length of 9 pixels. 
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green') #(J.H) Uses the square() function to draw a green square with a length of 9 at the (x,y) coordinates of the food block generated by the if head == food statement.

#Update Display:
    update()

#Game Loop:
    ontimer(move, 100)
#Uses the ontimer function to create a game loop, calling the move function every 100 milliseconds to continue the game.

setup(420, 420, None, None) #(J.H) The turtle.setup(width, height, x, y) function creates the dimensions of the game window and it's starting position on the screen of a computer. It is initialized to a 420x420 pixel width and height and it'll appear in the centre of a computer screen.
hideturtle() #(J.H) The hideturtle() function hides the cursor/arrow that appears whenever a line is drawn. We use this function to hide the cursor otherwise you'll see an arrow initializing the game window.
tracer(False) #(J.H) The tracer(n,delay) function from the Turtle module turns the turtle drawing animation on/off with the ability to take two arguments. n is an integer that'll tell the function to run every n-th screen update and the delay argument sets the interval between each update. We use False here to turn off this function and let the amount of screen updates and it's interval be determined by when an update() function is called and the ontimer() function to determine the interval. 
listen() #(J.H) The listen() function sets focus on the turtle screen and looks out for events (aka key presses) which compliments the next few lines of code.
onkey(lambda: change(10, 0), 'Right') #(J.H) The onkey() function calls a function when a certain key is pressed. Additionally, the lambda function is an anonymous function initalized by the keyword. The lambda function can take an argument 'lambda arguments: expression' but in this case we don't need it. However, we do leave an expression which is the change function. The lambda function takes the change function with the arguments of (10,0) which changes the snake's movement to the right evaluatues it and returns it, so it changes the variables, whenever the user presses the 'd' key.
onkey(lambda: change(-10, 0), 'Left') #(J.H) Using the onkey() function in combination with the lambda function, we can change the direction of the snake's movement with a simple expression and function. We assign that whenever the user presses the 'a' key it changes the aim vector's value to (-10,0) which changes the snake's movement to the left.
onkey(lambda: change(0, 10), 'Up') #(J.H) We assign that whenever the user presses the 'w' key it changes the aim vector's value to (0,10) which changes the snake's movement to the upward direction.
onkey(lambda: change(0, -10), 'Down') #(J.H) We assign that whenever the user presses the 's' key it changes the aim vector's value to (0,-10) which changes the snake's movement to the downward direction.
move() #(J.H) We call the main game function to initialize the game whenever this code file is ran.
done() #(J.H) This done() starts the loops of all turtle functions and methods and it must be at the end of code files containing turtle functions.
