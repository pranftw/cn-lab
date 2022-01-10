import socket
import json

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c.connect((socket.gethostname(), 58000))

filename = input("Enter the filename: ")
d = {'filename':filename}
d_json = json.dumps(d)
c.send(bytes(str(d_json),"utf-8"))
print(c.recv(1024).decode("utf-8"))
c.close()