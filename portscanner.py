import socket
from tqdm import tqdm
from IPy import IP

ports = []

def get_own_id():
    return str(socket.gethostbyname(socket.gethostname()))

def scan(target):
    global ports
    converted_ip = check_ip(target)
    print('\n[-_0 Scaning target]'+str(target))
    for port in tqdm(range(1, 500), desc="Port"):
        scan_port(converted_ip, port)
    return ports

def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress, port):
    global ports
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open Port' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port' + str(port))
        ports.append(port)
    except:
        #print('[-] Closed Port' + str(port))
        pass

if __name__ == '__main__':
    print('O IP Pode Ser Um Link Ou Um Numero.\n')
    targets = input("[+] Enter Target/s To Scan (split multiple targets with ,): ")
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)
