import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),58000))
s.listen(5)

print("Server up and running!")
while True:
    client_socket, client_address = s.accept()
    print(f"Address: {client_address}")
    client_msg = json.loads(client_socket.recv(1024).decode("utf-8"))
    try:
        fp = open(client_msg['filename'],"r")
        client_socket.send(bytes(fp.read(),"utf-8"))
        fp.close()
    except:
        client_socket.send(bytes("File not present!", "utf-8"))
    client_socket.close()