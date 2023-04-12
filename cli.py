# this file will display the command line interface for the user
import test_mode
import os # for clearing the screen

def print_menu():
    print("--------------------------------------------------")
    print("Welcome to the command line interface for the CODEV project")
    print("MENU:")
    print("1. Trajectory mode")
    print("2. Live mode")
    print("3. Test mode")
    print("4. Settings")
    print("5. Exit")


def main():
    os.system('cls' if os.name == 'nt' else 'clear') # clear the screen
    while True:
        print_menu()
        choice = int(input("Please enter a number: "))
        if choice == 1:
            print("Trajectory mode")
        elif choice == 2:
            print("Live mode")
        elif choice == 3:
            print("Test mode")
            test_mode.main()
        elif choice == 4:
            print("Settings")
        elif choice == 5:
            print("Exit")
            break
        else:
            print("Invalid input")
        os.system('cls' if os.name == 'nt' else 'clear') # clear the screen


main()
