import socket

HOST = '127.0.0.1'
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Server is waiting for a file on {HOST}:{PORT}...")

    conn, addr = s.accept()
    with conn:
        print(f"Accepting data from {addr}")
    
        with open('received_file.txt', 'wb') as f:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                f.write(data)
        
        print("File received and saved as 'received_file.txt'")