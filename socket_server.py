import socket

# Define host and port
HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 49152  # Port to listen on (non-privileged ports are > 1023)

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the host and port
    s.bind((HOST, PORT))
    # Listen for incoming connections
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")

    # Accept incoming connection
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            # Receive data from the client
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode()}")
            # Echo back the received data
            conn.sendall(data)
