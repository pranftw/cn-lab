import socket
import json

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((socket.gethostname(),58000))

filename = input("Enter the path of the file: ")
word = input("Enter the word: ")
d = {"filename":filename}
d_json = json.dumps(d)
c.send(bytes(str(d_json),"utf-8"))

msg = c.recv(1024)
print(msg.decode("utf-8"))
c.close()