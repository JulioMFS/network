import socket
HOST = 'sanfona.myvnc.com'  # The server's hostname or IP address
PORT = 49152        # The port used by the server
f = b'/media/julio/TOSHIBA EXT/C_Drive_23_03_2015/Htc/Storage Card/IMG-20120114-00031.jpg'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #s.sendall(b'Hello, world wwwwwwwwxxxxx')
    s.sendall(f)
    data = s.recv(1024)

print('Received', repr(data))