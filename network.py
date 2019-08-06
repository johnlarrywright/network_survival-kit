#!/usr/bin/python3

import socket
import argparse

def network():
    parser = argparse.ArgumentParser(
        prog ='IP Mapping',
        description='Command line IP mapping'
)

    parser.add_argument('domain', help='Require domain to get IP target')

    args= parser.parse_args()

    domain = args.domain

    return_ip = socket.getaddrinfo(domain, 443)

    print('Enter domain {}'.format(domain))
    print('The IP address of target is {}'.format(return_ip[0][4][0]))

if __name__ == "__main__":
    network()    