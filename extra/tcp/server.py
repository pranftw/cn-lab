import socket
import json
import re

fragment_size = 1024
port_no = 58000

def send_msg(sock, msg_str):
    sock.send(bytes(msg_str,"utf-8"))

if __name__=='__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(),port_no))

    s.listen(5)

    print("Server up and running!\n")
    while True:
        client_socket, client_address = s.accept()
        print(f"Address: {client_address}")
        msg_from_client = client_socket.recv(fragment_size).decode("utf-8")
        if msg_from_client:
            d = json.loads(msg_from_client)
            word_re = re.compile(d['word'])
            for fname in d['filenames']:
                try:
                    fp = open(fname, "r")
                    matches = word_re.findall(fp.read())
                    if matches:
                        send_msg(client_socket, f"{fname}: {len(matches)}")
                    else:
                        send_msg(client_socket, f"{fname}: 0")
                    fp.close()
                except:
                    send_msg(client_socket, f"{fname} File not present!")
        client_socket.close()
    