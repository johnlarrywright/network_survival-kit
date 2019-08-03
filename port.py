#!/usr/bin/python3
import sys
import socket
import argparse

parser = argparse.ArgumentParser(
    prog ='Port Scanner',
    description='Command line Scanning ports'
)

parser.add_argument('port_scanner', help='Require ip in order to scan for open ports')

args = parser.parse_args()

port_scanner = args.port_scanner