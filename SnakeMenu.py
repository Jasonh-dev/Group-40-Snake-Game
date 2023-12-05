#Jason Hui (J.H)
#Fatima Pina (F.P)

def display_menu():
    
    '''
    (J.H) The purpose of this function is to print the options that the user has
    and we made it a function so we're able to change the print options easily
    and it provides a more readable code.
    '''
    
    print("Menu:")
    print("[1] Single Player")
    print("[2] Two Player")
    print("[3] Quit")

def main():
    
    '''
    (J.H) This function contains the main loop for the purpose of a menu. It prompts
    the user for an input, from 1-3 and if it's an invalid input, it'll continue 
    to ask until an accepted value is entered.
    '''
    
    while True: 
        #(J.H.) We used a while loop as it allows us to run this menu function however many times it takes until an accepted value is entered
        display_menu() #(J.H) We call the function with all of the print statements to display to the user their options
        
        choice = input("Please enter your choice (1/2/3): ")
        #(J.H) The choice variable is set to the input of the user with a prompt for their desired game mode
        #(J.H) We use this variable to base conditions for our if statements to eventually import and run the corresponding game mode or exit the program.

        if choice == '1': 
            print("Single Player mode selected")
            import PSnake #These import commands are just importing the game file of the corresponding game mode that the user chose.
            break #This just breaks out of the while loop once the game has been imported and initalized which is done within the game file

        elif choice == '2':
            print("Two Player mode selected")
            import PPSnake
            break
        
        elif choice == '3':
            print("Quitting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option (1/2/3).")

if __name__ == "__main__": #This just runs the file if the file is ran explicitly/not imported
    main()
