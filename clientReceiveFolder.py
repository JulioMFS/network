import socket
import os

# Client configuration
#SERVER_HOST = '127.0.0.1'
SERVER_HOST = 'sanfona.myvnc.com'
SERVER_PORT = 49152
BUFFER_SIZE = 1024

# Main client function
def main():
    # Create socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT))

        # Get folder name from user
        #folder_name = input("Enter folder name to download: ")
        #folder_name = b'/media/julio/TOSHIBA EXT/C_Drive_23_03_2015/Htc/Storage Card/IMG-20120114-00031.jpg'
        #folder_name = '\\media\\julio\\TOSHIBAEXT\\C_Drive_23_03_2015\\Htc\\StorageCard\\'
        #folder_name = 'media/julio/TOSHIBA EXT/C_Drive_23_03_2015/Htc/Storage Card$'
        #folder_name = "/media/julio/TOSHIBA EXT/C_Drive_23_03_2015/Htc"
        folder_name = "/media/julio/TOSHIBA EXT/C_Drive_23_03_2015/"
        # Send folder name to server
        client_socket.sendall(folder_name.encode())

        # Receive server response
        response = client_socket.recv(BUFFER_SIZE).decode()

        if response == "OK":
            num_files = int(client_socket.recv(BUFFER_SIZE).decode())
            print(f'Found {num_files} in {folder_name}')
            # Create directory to store files if it doesn't exist
            if not os.path.exists(folder_name):
                print(f"\tPath: {folder_name} doesn't exist ")
                os.makedirs(folder_name)

            # Receive files from server
            for _ in range(num_files):
                filename = client_socket.recv(BUFFER_SIZE).decode()
                with open(os.path.join(folder_name, filename), 'wb') as file:
                    while True:
                        data = client_socket.recv(BUFFER_SIZE)
                        if not data:
                            break
                        print(f'\tWriting {os.path.join(folder_name, filename)}')
                        file.write(data)

            print("Folder downloaded successfully")

        else:
            print("Folder does not exist on the server")

if __name__ == "__main__":
    main()
