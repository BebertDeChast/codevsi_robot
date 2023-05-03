import communication


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
        # print("Reading...")
        # print(communication.read(communication.arduino))
    return
