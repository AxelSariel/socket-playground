import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('0.0.0.0', 5105))
    s.sendall(b"Hello world!")
    data = s.recv(1024)

print(f"Received {data!r}")