#Two Player Snake Game All Functions & Game Code
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

# Initialize game variables
food = vector(0, 0)
delay = 100
end_display = Turtle()
quit_display = Turtle()

# Initializes variables for Snake 1/Player 1
snake1 = [vector(10, 0)]
snake1_aim1 = vector(0, -10)
score1 = 0

# Initializes variables for the Snake 2/Player 2
snake2 = [vector(-10, 0)]
snake2_aim2 = vector(0, 10)
score2 = 0

# Initializes the size of the game window and background colour to black
setup(450, 450, None, None) #(J.H) The turtle.setup(width, height, x, y) function creates the dimensions of the game window and it's starting position on the screen of a computer. We made it 450 pixed in width and height, and made it appear in the centre of any screen.
bgcolor('black') #(J.H) The turtle.bgcolor() function sets the background colour for the turtle screen (game window). We made it to a simple black background colour.
hideturtle() #(J.H) The hideturtle() function hides the cursor/arrow that appears whenever a line is drawn. We use this function to hide the cursor otherwise you'll see an arrow initializing the game window.

#Creates the border of the game
def draw_border():
    border = Turtle() #(J.H) Creating a variable and calling the Turtle() class initializes an object that has methods with drawing & displaying text abilities. We use it here to draw the borders of the playable game space.
    border.hideturtle() #(J.H) The function ability was described before. We use this function to hide the cursor otherwise you'll see an arrow flying across to screen to draw the lines of the game border.
    border.penup() #(J.H) The penup() function disenables the drawing capability of the turtle. We use this function to not draw a line as we move the cursor to it's starting position which is described in the next line. 
    border.goto(200,200) #(J.H) The goto(x,y) function moves the cursor/turtle to an (x,y) coordinate. We made the cursor start at the top right coordinate of the border (200,200)
    border.color('magenta') #(J.H) The color() function generates the colour of the line. We made it magenta to make it stand out against the black background.
    border.pendown() #(J.H) The pendown() function enables the drawing capability of the cursor. We enable the cursor now as when we use another goto() command, we want the turtle to draw a line as that's what's gonna represent the border.
    border.goto(-200,200) #(J.H) We now tell the cursor to move along the 4 coordinates of the square to draw out the border, this is top left.
    border.goto(-200,-200) #(J.H) This is bottom left.
    border.goto(200,-200) #(J.H) This is bottom right.
    border.goto(200,200) #(J.H) This is the original position, top right.

draw_border() #(J.H) We call the function at the beginning of the game to show the cool animation/process of drawing the border right away.

#Creates the score display for Snake 1/Player 1
score_display = Turtle() 
score_display.hideturtle()
score_display.penup()
score_display.goto(-70, 200)
score_display.color('yellow')
score_display.write(f"P1 Score: {score1}", align="center", font=("Arial", 14, "normal")) #(J.H) This write() function provides the actual letters/words we see on the screen. The first argument is what's being outputted onto the screen and because the score for player 1 is being updated we use python f-string that allows us to embed changing values into our text, which in this case is the score. The other arguments configure the allignment, font, and size of the text.

#Creates the score display for Snake 2/Player 2
score_display2 = Turtle()
score_display2.hideturtle()
score_display2.penup()
score_display2.goto(70,200)
score_display2.color('cyan')
score_display2.write(f"P2 Score: {score2}", align="center", font=("Arial", 14, "normal"))

#Creates the display for informing the player on how to quit the game
def quit_info():
    quit_display.hideturtle()
    quit_display.penup()
    quit_display.goto(0,-25)

#Creates the game ending acknowledgement
def lose_display():
    end_display.hideturtle()
    end_display.penup()

def restart_game(): #(J.H) The restart_game() function restores the initial values onto important game variables that allows for a fresh game to start.
    global delay, score1, snake1, score2, snake2_aim2, snake2, snake1_aim1  #(J.H) The global keyword makes variables belong to the global scope. We use the global keyword here to access the game variables that we defined outside of this function that we have to restore original values to, to restart the game.
    delay = 100 #(J.H) We restore the delay variable to 100 miliseconds.
    
    score1 = 0 #(J.H) We restore the score of player1 to zero.
    snake1_aim1 = vector(0,-10) #(J.H) We restore the (x,y) values of the aim vector for player 1 to (0,-10)
    snake1 = [vector(10,0)] #(J.H) We restore the snake1/player1 list to only contain the original vector with an (x,y) value of (10,0)
    
    score2 = 0 #(J.H) We restore the score of player2 to zero.
    snake2_aim2 = vector(0, 10) #(J.H) We restore the (x,y) values of the aim vector for player 2 to (0,10)
    snake2 = [vector(-10,0)] #(J.H) We restore the snake2/player2 list to only contain the original vector with an (x,y) value of (-10,0)
    
    score_display.clear() #(J.H) We clear the score from the previous run of the game to allow for a fresh start
    score_display.write(f"P1 Score: {score1}", align="center", font=("Arial", 14, "normal")) #(J.H) We reinitalize/configure the text, it's allignment, size, and font.
    
    score_display2.clear() #(J.H) We clear the score from the previous run of the game to allow for a fresh start
    score_display2.write(f"P2 Score: {score2}", align="center", font=("Arial", 14, "normal")) #(J.H) We reinitalize/configure the text, it's allignment, size, and font.
    
    end_display.clear() #(J.H) We clear the game ending/restarting display to allow for a clear view of the new game.
    
    quit_display.clear() #(J.H) We clear the quitting info display to allow for a clear view of the new game.
    
    two_player() #(J.H) We call the main game function to start the new game.

def change1(x, y): #(J.H) This change1() function takes in two arguments (x,y) which will change the (x,y) value of the 2d vector that'll control the directional movement of player 1's snake. The specific keys are at the bottom of the page.
    snake1_aim1.x = x #(J.H) The vector.x() function changes the x-value of a two dimensional vector. We use this function to state that the x value in the vector defined by snake1_aim1 is equal to the first argument of the change function, which will be used/changed in the controls of player1 at the bottom of the code.
    snake1_aim1.y = y #(J.H) Using the vector.y() function we change the y-value of the two dimensional vector representing the y-direction movement of the snake by the y argument of the change function which will be changed by player 1's key presses shown at the bottom of the code.

def change2(x, y): #(J.H) This change2() function takes in two arguments (x,y) which will change the (x,y) value of the 2d vector that'll control the directional movement of player 2's snake. The specific keys are at the bottom of the page.
    snake2_aim2.x = x  #(J.H) Using the vector.x() function we change the x-value of the two dimensional vector representing the aim vector for player 2 to the x argument of the change function which will be changed by player 2's key presses shown at the bottom of the code.
    snake2_aim2.y = y #(J.H) Using the vector.y() function we change the y-value of the the aim vector for player 2 to the y argument of the change function which will be changed by player 2's key presses shown at the bottom of the code.

def two_player():
    head1 = snake1[-1].copy()
    head1.move(snake1_aim1)

    head2 = snake2[-1].copy()
    head2.move(snake2_aim2)

    global delay, score1, score2 

    if head1.x == 200: #(J.H) Using the copy of the snake vectors representing the head and body of player 1's snake, we check that if the x-value of the vector is = to 200
        head1.x = -200 #(J.H) We 'teleport' it to the other side of the screen which is the -200 value
    elif head1.x < -200: #(J.H) As well, we check that if the x-value of the vector is < -200
        head1.x = 190 #(J.H) We 'teleport' the snake to the other side of the game screen which is the 190 value
    if head1.y >= 200: #(J.H) These checks are the same but for the y-value. If the y-value of the vector representing the head and body of player1's snake is >= to 200
        head1.y = -200 #(J.H) Then we 'teleport' it to the bottom of the screen which is -200
    elif head1.y < -200: #(J.H) We check if the y-value of the vector is < -200 (bottom) and if it is
        head1.y = 190 #(J.H) We 'teleport' it to the top of the screen
    
    if head2.x == 200: #(J.H) Using the copy of the snake vectors representing the head and body of player 2's snake, we do the same checks that we did for player 1's snake.
        head2.x = -200 #(J.H) And if the x-value is = 200, we make it = -200, making it appear on the other side of the screen.
    elif head2.x < -200: #(J.H) The same concept as the if statement for head1 but it is being checked for player 2's snake. 
        head2.x = 190 #(J.H) And if the x-value is = 190, we make it = -190 which will 'teleport' it to the other side of the screen.
    if head2.y >= 200: #(J.H) These checks are the same concept from player 1's if statements but are for player 2's snake and its y-values.
        head2.y = -200 #(J.H) If the y-value is >= 200 we make it -200
    elif head2.y < -200: #(J.H) If the y-value is < -200 
        head2.y = 190 #(J.H) We make it 190
    
    lose_display()
    quit_info() 
    
    if head1 in snake1: #(J.H) This if statement checks whether or not the (x,y) value of the vector representing the head of player 1's snake is in the list snake1, which holds the vectors of the player 1's snake's body. 
        square(head1.x, head1.y, 9, 'red') #(J.H) If the vector representing the head is found in the snake's body list, then we use the square() function to draw a red sqaure with a side length of 9 at the (x,y) coordinate of the head.
        
        end_display.color('yellow') #(J.H) After calling the lose_display() function before this if statement we first initialize it's colour to yellow.
        end_display.write(f"Player 1 Loses! Restarting in 6 seconds...", align="center", font=("Arial", 14, "normal")) #(J.H) We then use the write() function to actually output text saying that player 1 lost and the game will automatically be restarting in 6 seconds. We've also configured the font, size, and allignment.
        
        quit_display.color('yellow') #(J.H) With the quitting information, we change the text colour to yellow.
        quit_display.write(f"Click on the screen at any time to end the game", align="center", font=("Arial", 14, "normal")) #(J.H) We use the write() function to display the quitting information to the user. We also configure the font, size, and allignment.
        
        ontimer(restart_game,6000) #(J.H) The ontimer() function calls a function after a certain time in miliseconds. We use this function to call the restart_game function to restart the game in 6 seconds (6000 miliseconds).
        exitonclick() #(J.H) The exitonclick() function quits the game window, so it closes everything down when a mouse click happens on screen. We use this function to enable the player to leave the game by clicking the screen.
        return
    elif head1 in snake2: #(J.H) This checks whether or not the (x,y) value of the vector representing the head of player 1's snake is in the list snake2, which hold the vectors representing the body squares of player 2's snake.
        square(head1.x, head1.y, 9, 'red') #(J.H) If the vector representing the head of player 1 is found in player 2's snake's body list, then we use the square() function to draw a red sqaure with a side length of 9 at the (x,y) coordinate of the head of player1's snake.
        
        end_display.color('yellow') #(J.H) We initialize the text colour to yellow for the losing acknowledgement
        end_display.write(f"Player 1 Loses! Restarting in 6 seconds...", align="center", font=("Arial", 14, "normal")) #(J.H) We use the write() function to actually output text saying that player 1 lost and the game will automatically be restarting in 6 seconds.
        
        quit_display.color('yellow') #(J.H) We change the text colour to yellow for the quitting information.
        quit_display.write(f"Click on the screen at any times to end the game", align="center", font=("Arial", 14, "normal")) #(J.H) We use the write() function to display the quitting information to the user.
        
        ontimer(restart_game,6000) #(J.H) To restart the game we call the restart function in 6 seconds (6000 miliseconds)
        exitonclick() #(J.H) A click on the screen enable the players to leave the game.
        return
    elif head2 in snake2: #(J.H) This checks if the head of player 2's snake is inside it's own body which is not allowed.
        square(head2.x, head2.y, 9, 'red') #(J.H) If  player 2's snake head is inside its own body, we use the square() function to draw a red sqaure with a side length of 9 at the (x,y) coordinate of the head.
        
        end_display.color('cyan') #(J.H) We change the text colour to cyan to represent player 2 for the losing information.
        end_display.write(f"Player 2 Loses! Restarting in 6 seconds...", align="center", font=("Arial", 14, "normal")) #(J.H) We use the write() function to actually output text saying that player 2 lost and the game will automatically be restarting in 6 seconds.
        
        quit_display.color('cyan') #(J.H) We change the text colour to cyan for homogeneity for the quitting information.
        quit_display.write(f"Click on the screen at any times to end the game", align="center", font=("Arial", 14, "normal")) #(J.H) We use the write() function to display the quitting information to the user.
        
        ontimer(restart_game,6000) #(J.H) Restarts the game in 6 seconds.
        exitonclick() #(J.H) Let's the user end the game no matter who wins or loses.
        return
    elif head2 in snake1: #(J.H) This checks if the head of player 2's snake is inside player 1's snake's body which is not allowed.
        square(head2.x, head2.y, 9, 'red') #(J.H) If player 2's snake head is inside player 1's snake's body, we use the square() function to draw a red sqaure with a side length of 9 at the (x,y) coordinate of the head.
        
        end_display.color('cyan') #(J.H) We change the text colour to cyan to represent player 2 for the losing information.
        end_display.write(f"Player 2 Loses! Restarting in 6 seconds...", align="center", font=("Arial", 14, "normal")) #(J.H) We use the write() function to actually output text saying that player 2 lost and the game will automatically be restarting in 6 seconds.
        
        quit_display.color('cyan') #(J.H) We change the text colour to cyan for homogeneity for the quitting information.
        quit_display.write(f"Click on the screen at any times to end the game", align="center", font=("Arial", 14, "normal")) #(J.H) We use the write() function to display the quitting information to the user.
        
        ontimer(restart_game,6000) #(J.H) Restarts the game in 6 seconds.
        exitonclick() #(J.H) Let's the user end the game
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

onkey(lambda: change1(10, 0), 'd') #(J.H) The onkey() function calls a function when a certain key is pressed. Additionally, the lambda function is an anonymous function initalized by the keyword. The lambda function can take an argument 'lambda arguments: expression' but in this case we don't need it. However, we do leave an expression which is the change function. The lambda function takes the change function with the arguments of (10,0) which changes the snake's movement to the right evaluatues it and returns it, so it changes the variables, whenever player 1 presses the 'd' key.
onkey(lambda: change1(-10, 0), 'a') #(J.H) Using the onkey() function in combination with the lambda function, we can change the direction of the snake's movement with a simple expression and function. We assign that whenever player 1 presses the 'a' key it changes the aim vector's value to (-10,0) which changes the snake's movement to the left.
onkey(lambda: change1(0, 10), 'w') #(J.H) We assign that whenever player 1 presses the 'w' key it changes the aim vector's value to (0,10) which changes the snake's movement to the upward direction.
onkey(lambda: change1(0, -10), 's') #(J.H) We assign that whenever player 1 presses the 's' key it changes the aim vector's value to (0,-10) which changes the snake's movement to the downward direction.

onkey(lambda: change2(10, 0), 'Right') #(J.H) We assign that whenever player 2 presses the right arrow key it changes player 2's snake's aim vector's value to (10,0) which changes the snake's movement to the right direction.
onkey(lambda: change2(-10, 0), 'Left') #(J.H) We assign that whenever player 2 presses the left arrow key it changes snake 2's aim vector's value to (-10,0) which changes the snake's movement to the left direction.
onkey(lambda: change2(0, 10), 'Up') #(J.H) We assign that whenever player 2 presses the up arrow key it changes the aim vector's value to (0,10) which changes the snake's movement to the upward direction.
onkey(lambda: change2(0, -10), 'Down') #(J.H) We assign that whenever player 2 presses the down arrow key it changes the aim vector's value to (0,-10) which changes the snake's movement to the downward direction.

two_player()
done()