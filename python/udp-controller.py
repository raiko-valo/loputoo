import socket
import keyboard

# HOST = '192.168.3.26'
HOST = '192.168.60.141'  # localhost
PORT = 12345  # Arbitrary non-privileged port

def send_data(host, port, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(message.encode('utf-8'), (host, port))
    client_socket.close()

def handle_controls():
    last_data_p1 = "P1 100 100 100 0;"
    last_data_p2 = "P2 100 100 100 0;"

    while True:

        # Initialize player data
        key_pressed_p1 = "P1"
        key_pressed_p2 = "P2"

        # Player 1 controls
        if keyboard.is_pressed('a') and not keyboard.is_pressed('d'):  # Left
            key_pressed_p1 += " 0"
        elif keyboard.is_pressed('d') and not keyboard.is_pressed('a'): # Right
            key_pressed_p1 += " 200"
        else:
            key_pressed_p1 += " 100"
        
        if keyboard.is_pressed('w') and not keyboard.is_pressed('s'):  # Up
            key_pressed_p1 += " 200"
        elif keyboard.is_pressed('s') and not keyboard.is_pressed('w'):  # Down
            key_pressed_p1 += " 0"
        else:
            key_pressed_p1 += " 100"

        if keyboard.is_pressed('x') and not keyboard.is_pressed('c'):  # Up
            key_pressed_p1 += " 200"
        elif keyboard.is_pressed('c') and not keyboard.is_pressed('x'):  # Down
            key_pressed_p1 += " 0"
        else:
            key_pressed_p1 += " 100"
        
        if keyboard.is_pressed('z'):  # a
            key_pressed_p1 += " 1;"
        else:
            key_pressed_p1 += " 0;"

        # Player 2 controls
        if keyboard.is_pressed('j') and not keyboard.is_pressed('l'):  # Left
            key_pressed_p2 += " 0"
        elif keyboard.is_pressed('l') and not keyboard.is_pressed('j'): # Right
            key_pressed_p2 += " 200"
        else:
            key_pressed_p2 += " 100"
        
        if keyboard.is_pressed('i') and not keyboard.is_pressed('k'):  # Up
            key_pressed_p2 += " 200"
        elif keyboard.is_pressed('k') and not keyboard.is_pressed('i'):  # Down
            key_pressed_p2 += " 0"
        else:
            key_pressed_p2 += " 100"

        if keyboard.is_pressed('n') and not keyboard.is_pressed('m'):  # Up
            key_pressed_p2 += " 200"
        elif keyboard.is_pressed('m') and not keyboard.is_pressed('n'):  # Down
            key_pressed_p2 += " 0"
        else:
            key_pressed_p2 += " 100"
        
        if keyboard.is_pressed(','):  # a
            key_pressed_p2 += " 1;"
        else:
            key_pressed_p2 += " 0;"

        if keyboard.is_pressed('e'):
            send_data(HOST, PORT, 'exit')
            break

        data_p1 = "".join(key_pressed_p1)
        data_p2 = "".join(key_pressed_p2)

        if data_p1 != last_data_p1:
            send_data(HOST, PORT, data_p1)
            last_data_p1 = data_p1

        if data_p2 != last_data_p2:
            send_data(HOST, PORT, data_p2)
            last_data_p2 = data_p2


if __name__ == "__main__":


    handle_controls()
