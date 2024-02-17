import socket

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"Server listening on {host}:{port}")

    while True:
        data, address = server_socket.recvfrom(1024)
        print(f"Received from {address}: {data.decode('utf-8')}")

if __name__ == "__main__":
    HOST = '127.0.0.1'  # localhost
    PORT = 12345  # Arbitrary non-privileged port
    start_server(HOST, PORT)
