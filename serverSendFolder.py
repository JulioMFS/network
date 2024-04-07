import socket
import os

# Server configuration
HOST = '127.0.0.1'
PORT = 49152
BUFFER_SIZE = 1024

# Function to send a file
def send_file(conn, filename):
    with open(filename, 'rb') as file:
        while True:
            data = file.read(BUFFER_SIZE)
            if not data:
                break
            conn.sendall(data)

# Main server function
def main():
    # Create socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        print("Server is listening...")

        while True:
            conn, addr = server_socket.accept()
            print(f"Connected to {addr}")

            # Receive folder name from client
            folder_name = conn.recv(BUFFER_SIZE).decode()
            print(f"Client requested folder: {folder_name}")

            # Check if folder exists
            if os.path.exists(folder_name) and os.path.isdir(folder_name):
                conn.sendall(b"OK")

                # Get list of files in the folder
                files = os.listdir(folder_name)
                conn.sendall(str(len(files)).encode())

                for filename in files:
                    conn.sendall(filename.encode())

                    # Send file
                    send_file(conn, os.path.join(folder_name, filename))

                print("Folder sent successfully")

            else:
                conn.sendall(b"Folder does not exist")
                print("Folder does not exist")

            conn.close()

if __name__ == "__main__":
    main()
