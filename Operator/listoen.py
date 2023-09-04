import socket
SERVER_HOST = '192.168.100.204'  # Replace with the IP address of the target cluster's Master
SERVER_PORT = 30006  # Port mapping of agent-service: 12345 -> 30006
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_HOST, SERVER_PORT))
    message = "Hello from the client!"
    s.sendall(message.encode())
    data = s.recv(1024)
print("Received:", data.decode())
