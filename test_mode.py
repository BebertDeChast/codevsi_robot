import communication
import time


def emiting_mode():
    '''
    This function will initialize the serial connection with the arduino \n
    Send custom instructions to the arduino and read the response
    '''
    communication.init()
    print("Starting complete")

    while True:
        data = input("Enter instruction (leave empty to exit): ")
        if data == "":
            break
        # if data == "s": #! Not working
        #     communication.stop()
        communication.write(data, communication.arduino)
        print("Instruction sent")
    return


def listening_mode():
    """
    This function will initialize the serial connection with the arduino \n
    Listen to the arduino and print the response with the time
    """

    communication.init()
    print("Starting complete")

    print("Reading...")
    while True:
        msg = communication.read(communication.arduino)
        print(time.ctime(time.time()))
        print(msg)

def test_puissance():
    communication.init()
    print("Starting complete")
    print("Reading...")
    t0 = time.time()
    t = t0
    data = open("log.txt", "a")
    data.write("# M0/M1/t\n")
    while True:
        msg = communication.read(communication.arduino)
        print(time.ctime(time.time()))
        print(msg)
        data.write(msg)