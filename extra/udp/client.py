import socket
import json
from server import send_msg, fragment_size, port_no

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c.connect((socket.gethostname(), port_no))

num_files = int(input("Enter the number of files: "))
filenames = []
for i in range(num_files):
    filenames.append(input(f"Enter filename {i}: "))
word = input("Enter the word: ")

d = {'filenames':filenames, 'word':word}
d_json = json.dumps(d)
send_msg(c, str(d_json))

msg_from_server = c.recv(1024).decode("utf-8")
print(msg_from_server)
c.close()