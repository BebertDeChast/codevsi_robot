# this file will display the command line interface for the user
import test_mode
import settings
import os  # for clearing the screen
import trajectory_mode


def print_menu():
    print("--------------------------------------------------")
    print("Welcome to the command line interface for the CODEV project")
    print("MENU:")
    print("1. Trajectory mode")
    print("2. Live mode")
    print("3. Test mode")
    print("4. Settings")
    print("5. Listening mode")
    print("6. Test puissance")


def main():
    '''Main function
    This function will display the command line interface
    '''
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # clear the screen
        print_menu()
        try:
            choice = input("Please enter a number (leave empty to exit): ")
        except ValueError:
            print("Invalid input")
            continue
        if choice == "":
            os.system('cls' if os.name == 'nt' else 'clear')  # clear the screen
            break
        
        choice = int(choice)
        if choice == 1:
            print("--------------------------------------------------")
            print("Trajectory mode")
            trajectory_mode.main()
        elif choice == 2:
            print("--------------------------------------------------")
            print("Live mode not implemented yet")
            input("Press enter to continue...")
        elif choice == 3:
            print("--------------------------------------------------")
            print("Emiting mode")
            test_mode.emiting_mode()
        elif choice == 4:
            settings.main()
        elif choice == 5:
            print("--------------------------------------------------")
            print("Listening mode")
            test_mode.listening_mode()
        elif choice == 6:
            print("--------------------------------------------------")
            print("Test puissance")
            test_mode.test_puissance()
        else:
            print("Invalid input")


main()
