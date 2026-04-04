import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 5123

client.connect((host, port))

massage = "Hello Server"
client.send(massage.encode())

data = client.recv(1024).decode()
print("Massage from server:", data)

client.close()