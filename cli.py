# this file will display the command line interface for the user
import test_mode
import settings
import os  # for clearing the screen


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
    '''Main function
    This function will display the command line interface
    '''
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # clear the screen
        print_menu()
        try:
            choice = int(input("Please enter a number: "))
        except ValueError:
            print("Invalid input")
            continue
        if choice == 1:
            print("--------------------------------------------------")
            print("Trajectory mode")
            input("Press enter to continue...")
        elif choice == 2:
            print("--------------------------------------------------")
            print("Live mode")
            input("Press enter to continue...")
        elif choice == 3:
            print("--------------------------------------------------")
            print("Test mode")
            test_mode.main()
        elif choice == 4:
            settings.main()
        elif choice == 5:
            print("Goodbye!")
            print("--------------------------------------------------")
            os.system('cls' if os.name == 'nt' else 'clear')  # clear the screen
            break
        else:
            print("Invalid input")


main()
