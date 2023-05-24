import serial
import time
import serial.tools.list_ports

com_port = None
debit = 9600


def detect_arduino(debug=False):
    '''Detect arduino function\n
    This function will detect the arduino and return the port
    '''
    ports = serial.tools.list_ports.comports()
    if debug:
        for port in ports:
            print(port.description)
    for port in ports:
        if "Arduino" in port.description:
            print("Arduino found on port: " + port.device)
            return port.device
        if "USB Serial" in port.description:
            print("XBee found on port: " + port.device)
            return port.device
        else:
            print("Device not found")
            return None


def write(x: str, target):  # write a string to the arduino
    target.write(bytes(x, 'utf-8'))


def read(target) -> str:
    """Read a string from the arduino and return it\n
    return None if no data is available"""
    data = target.readline()  # need an \n to end the line and stop communication
    if data.endswith(b'\n'):  # remove \n if there is one
        data = data[:-1]
    if data:
        return data.decode("utf-8")


def create_string(intruction: list) -> str:
    """Generate a string to send to the arduino \n
    based on the dictionnary of speed instruction \n
    input format:
    [[vitesseG (m/s), vitessD (m/s)],temps(ms))] \n
    format:
    SD/Dvitesse(b3)/SG/Gvitesse(%)/temps(ms)"""
    # if mode != "l" and mode != "r":
    # raise ValueError("mode must be 'l'(live) or 'r'(remote)")
    if len(intruction) != 2 and len(intruction[0]) != 2:
        raise ValueError("intruction must be a list of a list and a float")
    # print(intruction)
    SG = int(intruction[0][0] > 0)
    SD = int(intruction[0][1] > 0)
    vd = int(abs(intruction[0][0]) * 100)
    vg = int(abs(intruction[0][1]) * 100)
    t = int(intruction[1] * 100)
    return f"/{SD}/{vd}/{SG}/{vg}/{t}"


def prepare_instruction(instruction: list, mode: chr = 'r') -> str:
    """
    instruction format:
    [[[vg, vd], dt], ...]
    """
    if mode != "l" and mode != "r":
        raise ValueError("mode must be 'l'(live) or 'r'(remote)")

    if mode == 'r':
        msg = "r"
        print(f"Sending {len(instruction)} instructions")
        for i in instruction:
            msg += create_string(i)
        print(msg)
        return msg
    if mode == 'l':
        msg = "l" + create_string(instruction[1])
        return msg


def send_instruction(instructions: list, mode: chr = 'r'):
    '''Send instruction function\n
    intruction format:
    [[[vg, vd], dt], ...] \n
    This function will send the instruction to the arduino'''
    write(prepare_instruction(instructions, mode), arduino)


def init():
    '''
    This function will initialize the serial connection with the arduino and will test it
    '''
    global arduino
    com_port = detect_arduino()
    if com_port is None:
        print("No device found")
        exit()
    try:
        arduino = serial.Serial(port=com_port, baudrate=debit, timeout=5)
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
        print("Device does not respond correctly")
    else:
        print("Device is ready")
