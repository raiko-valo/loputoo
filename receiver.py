import socket
import json
import vgamepad as vg

def gamepad_controller(gamepad, data):
    x_value_float = int(data[3]) - int(data[0])
    y_value_float = int(data[1]) - int(data[2])
    gamepad.left_joystick_float(x_value_float=x_value_float, y_value_float=y_value_float)

    if data[4] == '1':
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
    if data[5] == '1':
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
    if data[6] == '1':
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    if data[7] == '1':
        gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    else:
        gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)

    gamepad.update()  # Send the updated state to the gamepad

        

def main():
    gamepad_p1 = vg.VX360Gamepad()
    gamepad_p2 = vg.VX360Gamepad()

    host = '0.0.0.0'
    port = 12345

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()

            print(f"Waiting for connection on {host}:{port}")
            conn, addr = s.accept()
            conn.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 2048)  # Set buffer size to 8 KB

            with conn:
                print(f"Connected by {addr}")
                old_data_p1, old_data_p2 = "", ""

                while True:
                    received_bytes  = conn.recv(1024)  # Adjust the buffer size as needed
                    if not received_bytes:
                        break

                    try:
                        gamepad_data = received_bytes.decode()

                        print(gamepad_data)

                        data_p1, data_p2 = gamepad_data.split("-")

                        if old_data_p1 != data_p1:
                            gamepad_controller(gamepad_p1, data_p1)
                            old_data_p1 = data_p1
                    
                        if old_data_p2 != data_p2:
                            gamepad_controller(gamepad_p2, data_p2)
                            old_data_p2 = data_p2

                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON: {e}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
