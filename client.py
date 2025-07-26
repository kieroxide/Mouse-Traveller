import socket

HOST = '192.168.0.25' 
PORT = 50000


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = s.recv(1024) 
        if not data:
            break 
        print(f"Received: {data.decode()}")
