#!/usr/bin/python3
import sys
import socket
import argparse

def port():
    parser = argparse.ArgumentParser(
        prog ='Port Scanner',
        description='Command line Scanning ports'
)

    parser.add_argument('ip', help='Require ip in order to scan for open ports')

    args = parser.parse_args()

    ip_scan = args.ip

#open_ports = socket.gethostbyname(port_scanner)
#family = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#result = family.connect(('68.66.200.198', 443))

    for port_scan in range(78, 130):
        family = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        family.settimeout(1)
    
        try:
            family.connect((ip_scan, port_scan))
    
            print('Port OPEN', port_scan)
        except:
            print('Port is closed!!!!')
    
if __name__ == "__main__":
    port()
#print('Enter ip address {}'.format(port_scanner))
#print('Enter IP address {}'.format(open_ports))
#print('Enter ip address {}'.format(port_scanner))


