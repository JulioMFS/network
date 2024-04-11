import os
import socket

from Cryptodome.Cipher import AES

key = b"TheNeuralNineLey"
nonce = b"TheNeuralNineNce"

cipher = AES.new(key, AES.MODE_EAX, nonce)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

file_size = os.path.getsize("C:\\Users\\julio\\OneDrive\\P D F\\casamento da estela\\casamento da estela 005.jpg")

with open("C:\\Users\\julio\\OneDrive\\P D F\\casamento da estela\\casamento da estela 005.jpg", "rb") as f:
    data = f.read()

encrypted = cipher.encrypt(data)

client.send("C:\\Users\\julio\\OneDrive\\P D F\\casamento da estela\\casamento da estela 005.jpg".encode())
client.send(str(file_size).encode())
client.sendall(encrypted)
client.send(b"<END>")

client.close()
