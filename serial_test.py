import serial
import time
arduino = serial.Serial(port='COM6', baudrate=9600, timeout=10)
time.sleep(1)  # wait for the serial connection to initialize


def write(x): # write a string to the arduino
    arduino.write(bytes(x, 'utf-8'))


def read(): # read a string from the arduino
    data = arduino.readline()[:-1]
    if data:
        return data


def main():
    # make a loop  to read the data from the arduino
    while True:
        
        send = input("Enter a value: ")
        if send == "exit": # exit the loop
            break
        t1 = time.time()
        write(send)
        print("Sent: " + send)
        data = read()
        print("Received: " + str(data))
        t2 = time.time()
        print("Time: " + str(t2 - t1) +"\n")

main()
