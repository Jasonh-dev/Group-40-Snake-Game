#One Player Snake Game All Functions & Game Code
#Jason Hui (J.H)
#Fatima Pina (F.P)


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

# Initializes game variables
food = vector(0, 0) #(F.P) This variable will represent the coordinates of the food 
delay = 100 #(F.P) Used to control the speed of the snake
end_display = Turtle() #(F.P) Using a turtle object to display the message for when the game ends
quit_display = Turtle() #(F.P) Using a turtle object to display intructions for quitting the game

# Initializes variables for Snake 1/Player 1
snake = [vector(10, 0)] #(F.P) Single vector used for the snake's head
aim = vector(0, -10) #(F.P) Represents the direction in which the snake is moving
score = 0 #(F.P) This variable will keep track of the score
    
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

#Creates the score display for the player
score_display = Turtle() #(F.P) It will display the player's score using the turtle module
score_display.hideturtle() 
score_display.penup()
score_display.goto(0, 200)
#(F.P) Score displays at the top center of the game
score_display.color('yellow') 
score_display.write(f"Score: {score}", align="center", font=("Arial", 14, "normal")) #(J.H) This write() function provides the actual letters/words we see on the screen. The first argument is what's being outputted onto the screen and because the score is being updated we use python f-string that allows us to embed changing values into our text, which in this case is the score. The other arguments configure the allignment, font, and size of the text.

#Creates the display for informing the player on how to quit the game
def quit_info():
    quit_display.hideturtle()
    quit_display.penup()
    quit_display.goto(0,-25)

#Creates the game ending acknowledgement
def lose_display():
    end_display.hideturtle()
    end_display.penup()
    
def change(x, y):
    aim.x = x #(J.H) The vector.x() function changes the x-value of the two dimensional vector. We use this function to state that the x value in the vector defined by aim is equal to the first argument of the change function, which will be used/changed in the controls of the player at the bottom of the code.
    aim.y = y #(J.H) The vector.y() function changes the y-value of the two dimensional vector. We use this function to state that the y value in the vector defined by aim is equal to the second argument of the change function, which will be used/changed in the controls of the player at the bottom of the code.

def restart_game(): #(J.H) The restart_game() function restores the initial values onto important game variables that allows for a fresh game to start.
    
    global delay, score, aim, snake #(J.H) The global keyword makes variables belong to the global scope. We use the global keyword here to access the game variables that we defined outside of this function that we have to restore original values to, to restart the game.
    
    delay = 100 #(J.H) We restore the delay variable to 100 miliseconds.
    score = 0 #(J.H) We restore the score to zero.
    aim = vector(0,-10) #(J.H) We restore the (x,y) values of the aim vector to (0,-10)
    snake = [vector(10,0)] #(J.H) We restore the snake list to only contain the original vector with an (x,y) value of (10,0)
    
    score_display.clear() #(J.H) We clear the score from the previous run of the game to allow for a fresh start
    score_display.write(f"Score: {score}", align="center", font=("Arial", 14, "normal")) #(J.H) We reinitalize/configure the text, it's allignment, size, and font.
    
    end_display.clear() #(J.H) We clear the game ending/restarting display to allow for a clear view of the new game.
    
    quit_display.clear() #(J.H) We clear the quitting info display to allow for a clear view of the new game.
    
    one_player() #(J.H) We call the main game function to start the new game.

def one_player():
    
    head = snake[-1].copy() #(F.P) The function creates a copy of the last segment that is, the head. 
    head.move(aim) #(F.P) Moves the head 
    
    global delay, score
    
    if head.x == 200: #(J.H) Using the copy of the snake vectors representing the head and body of the snake, we check that if the x-value of the vector is = to 200 (far right)...
        head.x = -200 #(J.H) We 'teleport' it to the other side of the screen which is the -200 value
    elif head.x < -200: #(J.H) As well, we check that if the x-value of the vector is < -200 (far left)...
        head.x = 190 #(J.H) We 'teleport' the head to the other side of the game screen which is the 190 value
        
    if head.y == 200: #(J.H) These checks are the same but for the y-value. If the y-value of the vector representing the head and body of the snake is = to 200 (top)...
        head.y = -200 #(J.H) Then we 'teleport' it to the bottom of the screen which is -200
    elif head.y < -200: #(J.H) We check if the y-value of the vector is < -200 (bottom) and if it is...
        head.y = 190 #(J.H) We 'teleport' it to the top of the screen
    
    lose_display()
    quit_info()
    
    if head in snake: #(J.H) This if statement checks whether or not the (x,y) value of the vector representing the head of the snake is in the list snake, which holds vectors of the snake's body. 
        square(head.x, head.y, 9, 'red') #(J.H) If the vector representing the head is found in the snake list, then we use the square() function to draw a red sqaure with a side length of 9 at the (x,y) coordinate of the head.
        
        end_display.color('yellow') #(J.H) After calling the lose_display() function before this if statement we first initialize it's colour to yellow.
        end_display.write("You Lose! Restarting in 6 seconds...", align="center", font=("Arial", 14, "normal")) #(J.H) We then use the write() function to actually output text saying that the player lost and the game will automatically be restarting in 6 seconds. We've also configured the font, size, and allignment.
        
        quit_display.color('yellow') #(J.H) With the quitting information, we change the text colour to yellow.
        quit_display.write("Click on the screen at any time to end the game", align="center", font=("Arial", 14, "normal")) #(J.H) We use the write() function to display the quitting information to the user. We also configure the font, size, and allignment.
        
        ontimer(restart_game,6000) #(J.H) The ontimer() function calls a function after a certain time in miliseconds. We use this function to call the restart_game function to restart the game in 6 seconds (6000 miliseconds).
        exitonclick() #(J.H) The exitonclick() function quits the game window, so it closes everything down when a mouse click happens on screen. We use this function to enable the player to leave the game by clicking the screen.
        
        return
    
    snake.append(head) #(F.P) Adds the new head to the snake's body
    
    if head == food:
        score += 1 #(F.P) Increments the score by 1 when the position of the snake's head is the same as the food
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Arial", 14, "normal")) #(F.P) Updates the display with the new score using the write() function
        
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        #(F.P) Generates new random coordinates for the next food square
        delay -= 5 #(F.P)Decreases the delay so that the speed of the snake will increase
    else:
        snake.pop(0) #(F.P) When the snake does not eat the food, it just keeps going straight. The pop() function, removes and return an element at the specific index. It is removing the tail of the snake
        
        clear()

    for body in snake:
        square(body.x, body.y, 9, 'yellow') #(F.P) Draws the snake's body in color yellow
    
    square(food.x, food.y, 9, 'green') #(F.P) Draws the food square in color green
    update()
    ontimer(one_player, delay)

tracer(False)
listen()
onkey(lambda: change(10, 0), 'd') #(F.P) Changes snake direction to the right. The onkey () function defines action in response to key presses. Whenever the user presses 'd', it executes the callback function (lambda). The change function updates the aim vector which is the direction of the snake
onkey(lambda: change(-10, 0), 'a') #(F.P) Chnages snake direction to the left 
onkey(lambda: change(0, 10), 'w') #(F.P) Changes snake direction up
onkey(lambda: change(0, -10), 's') #(F.P) Changes snake idrection down
one_player() 
done()
