import serial
import time

com_port = 'COM6'
debit = 9600


def write(x):  # write a string to the arduino
    arduino.write(bytes(x, 'utf-8'))


def read():  # read a string from the arduino
    """Read a string from the arduino and return it
    return None if no data is available"""
    data = arduino.read()
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
    write(compile_data(d_instrustion, g_instrustion, mode))


arduino = serial.Serial(port=com_port, baudrate=debit, timeout=10)
time.sleep(1)  # wait for the serial connection to initialize
print("Connecting to: " + arduino.portstr)

# test if the arduino is ready
t1 = time.time()
write("t")
test = read()
t2 = time.time()
print("Delay: " + str(t2 - t1))
if test != "k":
    print("Arduino is not ready")
    exit()
else:
    print("Arduino is ready")
