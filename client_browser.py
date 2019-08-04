#!/usr/bin/python3

import urllib.request
import argparse

parser = argparse.ArgumentParser(
    prog ='Client Browser',
    description='Command line Client Browser'
)

parser.add_argument('client', help='Enter domain for browser')

args = parser.parse_args()

client = args.client

url = urllib.request.urlopen(client)

#print(url.read())
print(url.geturl())
print(url.info())
print(url.getcode())
