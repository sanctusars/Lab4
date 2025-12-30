import socket

HOST = '127.0.0.1'
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = "Some data"
    print(f"Sending: {message}")
    s.sendall(message.encode('utf-8'))
    
    data = s.recv(1024)

print(f"Received response from server: {data.decode('utf-8')}")