import socket
domains = input("Enter 4 domain name: ").split()
if len(domains) != 4:
    print("Please enter 4 domain name")
else:
    for i in domains:
        try:
            ip = socket.gethostbyname(i)
            print(f"{i} --> {ip}")
        except:
            print(f"Domain Connection Error!")