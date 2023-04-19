import serial
import time
import serial.tools.list_ports

com_port = None
debit = 9600


def detect_arduino():
    '''Detect arduino function
    This function will detect the arduino and return the port
    '''
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if "Arduino" in port.description:
            print("Arduino found on port: " + port.device)
            return port.device
        else:
            print("Arduino not found")
            return None


def write(x, target):  # write a string to the arduino
    target.write(bytes(x, 'utf-8'))


def read(target):  # read a string from the arduino
    """Read a string from the arduino and return it
    return None if no data is available"""
    data = target.read()
    if data:
        return data.decode("utf-8")


def compile_data(d_instrustion: dict, g_instrustion: dict, mode: chr = 'r'):
    """Generate a string to send to the arduino
    format:
    mode/D.vitesse(b3).temps(ms)/G.vitesse(b3).temps(ms)"""
    if mode != "l" and mode != "r":
        raise ValueError("mode must be 'l'(live) or 'r'(remote)")
    return f"{mode}/{d_instrustion['vitesse']}.{d_instrustion['temps']}/{g_instrustion['vitesse']}.{g_instrustion['temps']}"


def send_instruction(d_instrustion: dict, g_instrustion: dict, mode: chr = 'r'):
    '''Send instruction function
    This function will send the instruction to the arduino'''
    write(compile_data(d_instrustion, g_instrustion, mode))


def main():
    '''Main function
    This function will initialize the serial connection with the arduino'''
    com_port = detect_arduino()
    try:
        arduino = serial.Serial(port=com_port, baudrate=debit, timeout=10)
    except serial.SerialException:
        print(f"Arduino not found on port: {com_port}")
        exit()

    time.sleep(1)  # wait for the serial connection to initialize
    print("Connecting to: " + arduino.portstr)

    # test if the arduino is ready
    t1 = time.time()
    write("t", arduino)
    test = read(arduino)
    t2 = time.time()
    print("Delay: " + str(t2 - t1))
    if test != "k":
        print("Arduino is not ready")
        exit()
    else:
        print("Arduino is ready")
