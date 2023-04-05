from communication import *

def main():
    print("Starting complete")
    d_instruction_test = {"vitesse": 100, "temps": 1000,}
    g_instruction_test = {"vitesse": -100, "temps": 1000,}

    send_instruction(d_instruction_test, g_instruction_test)


    return

main()