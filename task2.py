import socket
import sys

HOST = '127.0.0.1'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.settimeout(1.0) 

try:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server started on {HOST}:{PORT}")

    while True:
        try:
            conn, addr = s.accept()
            conn.settimeout(None) 
            
            with conn:
                print(f"\nNew connection: {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data: break
                    conn.sendall(data)
        
        except socket.timeout:
            continue

except KeyboardInterrupt:
    print("\nServer stopped by user.")

finally:
    s.close()
    sys.exit(0)