import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((socket.gethostname(),58000))

print("Server up and running!")
while(True):
    msg, client_address = s.recvfrom(1024)
    print(f"Address: {client_address}")
    client_msg = json.loads(msg.decode("utf-8"))
    try:
        fp = open(client_msg['filename'],"r")
        s.sendto(bytes(fp.read(),"utf-8"),client_address)
        fp.close()
    except:
        s.sendto(bytes("File not present!","utf-8"),client_address)