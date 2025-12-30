import socket

HOST = '127.0.0.1' 
PORT = 8000        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server started on {HOST}:{PORT} and waiting for connections...")
    
    conn, addr = s.accept()
    with conn:
        print(f"Connected to client: {addr}")
        
        while True:
            data = conn.recv(1024)
            
            if not data:
                break
            print(f"Received: {data.decode('utf-8')}")
            conn.sendall(data)