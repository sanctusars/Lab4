import socket
import os

HOST = '127.0.0.1'
PORT = 8000
FILENAME = 'test.txt'

if not os.path.exists(FILENAME):
    with open(FILENAME, 'w', encoding='utf-8') as f:
        f.write("Some file content.")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        print(f"Connected to the server. Sending file: {FILENAME}")

        with open(FILENAME, 'rb') as f:
            chunk = f.read(1024)
            while chunk:
                s.sendall(chunk)
                chunk = f.read(1024)
        
        print("File sending completed.")
    except ConnectionRefusedError:
        print("Error: Server is not running!")