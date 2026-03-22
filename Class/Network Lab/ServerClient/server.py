import socket
server_scoket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host  = 'localhost'
port = 3000
server_scoket.bind((host, port))
server_scoket.listen(1)
print("Server is watting to connect")
conn, addr = server_scoket.accept()
print("Connect to: ", addr)
data = conn.recv(1024).decode()
print("Massage of Client: ",data)
massage = "Hello Client massage recived"
conn.send(massage.encode())
conn.close()
