#!/usr/bin/python3

import socket
import argparse
#This tool will grab the hostname of the target machine.
parser = argparse.ArgumentParser(
    prog='system-tool',
    description='Command line system-tool'
)

parser.add_argument("ip", help="Require ip to look up hostname")
#parser.add_argument('--scan', help='Number of execution threads')
args = parser.parse_args()
ip = args.ip

hostname = socket.gethostbyaddr(ip)
print('Hostname of target machine {}'.format(ip))
print('Local host is {}'.format(hostname [0]))


