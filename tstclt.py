# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
#HOST = "192.168.131.10" # The server's IP address
#HOST = "192.168.155.100"
PORT = 65432  # The port used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"WAHEED")
    data = s.recv(1024)

print(f"Received {data!r}")
