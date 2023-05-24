import communication
import time


def main():
    '''Main function
    This function will initialize the serial connection with the arduino
    Send custom instructions to the arduino and read the response'''
    communication.main()
    print("Starting complete")

    while True:
        data = input("Enter instruction (leave empty to exit): ")
        if data == "":
            break
        communication.write(data, communication.arduino)
        print("Instruction sent")
    return


def listening_mode():
    communication.main()
    print("Starting complete")

    print("Reading...")
    while True:
        msg = communication.read(communication.arduino)
        print(time.ctime(time.time()))
        print(msg)
