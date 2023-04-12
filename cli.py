# this file will display the command line interface for the user
import test_mode
import communication
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


def print_settings():
    print("--------------------------------------------------")
    print("Settings")
    print("1. COM port")
    print("2. Baudrate")
    print("3. Back")


def settings():
    while True:
        print_settings()
        choice = int(input("Please enter a number: "))
        if choice == 1:
            print("COM port")
            print(f"Current com port: {communication.com_port}")
            communication.com_port = input("Please enter the COM port: ")
            if communication.com_port == "":
                communication.com_port = "COM6"
            print(f"New com port: {communication.com_port}")
        elif choice == 2:
            print("Baudrate")
            print(f"Current baudrate: {communication.debit}")
            communication.debit = input("Please enter the baudrate: ")
            if communication.debit == "":
                communication.debit = 9600
            print(f"New baudrate: {communication.debit}")
        elif choice == 3:
            break
        else:
            print("Invalid input")


def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # clear the screen
        print_menu()
        choice = int(input("Please enter a number: "))
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
            settings()
        elif choice == 5:
            print("Goodbye!")
            print("--------------------------------------------------")
            break
        else:
            print("Invalid input")


main()
