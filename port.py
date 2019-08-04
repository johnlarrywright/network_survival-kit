#!/usr/bin/python3
import sys
import socket
import argparse

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

for port_scan in range(1, 10):
    family = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    family.settimeout(1)
    print('socket created')
    try:
        result = family.connect(('13.33.147.123', 443))
    
        print('Port 80: OPEN', family)
    except:
        print('timeout')
    

#print('Enter ip address {}'.format(port_scanner))
#print('Enter IP address {}'.format(open_ports))
#print('Enter ip address {}'.format(port_scanner))


