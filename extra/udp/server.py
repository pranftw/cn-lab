import socket
import json
import re

fragment_size = 1024
port_no = 58000

def send_msg(sock, msg_str):
    sock.send(bytes(msg_str,"utf-8"))

if __name__=='__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((socket.gethostname(),port_no))

    print("Server up and running!")
    while True:
        msg, client_address = s.recvfrom(fragment_size)
        print(f"Address: {client_address}")
        client_message = msg.decode("utf-8")
        if client_message:
            d = json.loads(client_message)
            word_re = re.compile(d['word'])
            for fname in d['filenames']:
                try:
                    fp = open(fname, "r")
                    matches = word_re.findall(fp.read())
                    if matches:
                        s.sendto(bytes(f"{fname}: PRESENT","utf-8"),client_address)
                    else:
                        s.sendto(bytes(f"{fname}: ABSENT","utf-8"),client_address)
                    fp.close()
                except:
                    s.sendto(bytes(f"{fname} File not present!"))