def display_menu():
    print("Menu:")
    print("[1] Single Player")
    print("[2] Two Player")
    print("[3] Quit")

def main():
    while True:
        display_menu()
        choice = input("Please enter your choice (1/2/3): ")

        if choice == '1':
            print("Single Player mode selected")
            import PSnake
            break

        elif choice == '2':
            print("Two Player mode selected")
            import PPSnake
            break
        elif choice == '3':
            print("Quitting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option (1/2/3).")

if __name__ == "__main__":
    main()
