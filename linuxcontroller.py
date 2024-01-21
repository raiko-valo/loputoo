import keyboard
import socket
import struct
import json

def input_handling(socket_connection):
    last_data_p1 = ""
    last_data_p2 = ""

    while True:
        key_pressed_p1 = list('0000000000')
        key_pressed_p2 = list('0000000000')

        # Player 1 controls
        if keyboard.is_pressed('a'):  # Left
            key_pressed_p1[0] = '1'
        if keyboard.is_pressed('w'):  # Up
            key_pressed_p1[1] = '1'
        if keyboard.is_pressed('s'):  # Down
            key_pressed_p1[2] = '1'
        if keyboard.is_pressed('d'):  # Right
            key_pressed_p1[3] = '1'
        if keyboard.is_pressed('q'):  # dpad up
            key_pressed_p1[4] = '1'
        if keyboard.is_pressed('e'):  # dpad down
            key_pressed_p1[5] = '1'
        if keyboard.is_pressed('z'):  # a
            key_pressed_p1[6] = '1'
        if keyboard.is_pressed('x'):  # b
            key_pressed_p1[7] = '1'

        # Player 2 controls
        if keyboard.is_pressed('j'):  # Left
            key_pressed_p2[0] = '1'
        if keyboard.is_pressed('i'):  # Up
            key_pressed_p2[1] = '1'
        if keyboard.is_pressed('k'):  # Down
            key_pressed_p2[2] = '1'
        if keyboard.is_pressed('l'):  # Right
            key_pressed_p2[3] = '1'
        if keyboard.is_pressed('u'):  # dpad up
            key_pressed_p2[4] = '1'
        if keyboard.is_pressed('o'):  # dpad down
            key_pressed_p2[5] = '1'
        if keyboard.is_pressed('n'):  # a
            key_pressed_p2[6] = '1'
        if keyboard.is_pressed('m'):  # b
            key_pressed_p2[7] = '1'

        data_p1 = "".join(key_pressed_p1)
        data_p2 = "".join(key_pressed_p2)

        if data_p1 != last_data_p1 or data_p2 != last_data_p2:
            output = data_p1 + "-" + data_p2
            print(output)
            socket_connection.send(output.encode())
            last_data_p1 = data_p1
            last_data_p2 = data_p2

def main():
    host = '127.0.0.1'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"Connected to {host}:{port}")
        s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 2048)
        s.connect((host, port))

        try:
            input_handling(s)
        except KeyboardInterrupt:
            print("Exiting...")

if __name__ == "__main__":
    main()
