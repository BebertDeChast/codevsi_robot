import communication
import trajectoire as trajectoire


def main():
    '''Main function
    This function will initialize the serial connection with the arduino\n
    Send custom instructions to the arduino and read the response'''
    communication.init()
    print("Starting complete")

    while True:
        data = input("Format of input [[LIN|ROT|CIR|BACK, param1, param2, param3], ...]\n Enter instruction (leave empty to exit): ")
        if data == "":
            break
        traj = trajectoire.get_trajectoire(eval(data))
        communication.send_instruction(traj)
        print("Instruction sent")
        # print("Reading...")
        # print(communication.read(communication.arduino))
    return