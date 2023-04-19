import communication


def print_settings():
    print("--------------------------------------------------")
    print("Settings")
    print("1. COM port")
    print("2. Baudrate")
    print("3. Back")


def main():
    '''Settings function
    This function will display the settings menu
    '''
    while True:
        print_settings()
        choice = int(input("Please enter a number: "))
        if choice == 1:
            print("COM port")
            print(f"Current com port: {communication.com_port}")
            communication.com_port = input("Please enter the COM port: ")
            if communication.com_port == "":
                communication.com_port = communication.detect_arduino()
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
