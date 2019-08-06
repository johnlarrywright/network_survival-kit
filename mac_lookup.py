#!/usr/bin/python3

import argparse
import urllib.request
import json
import codecs

parser = argparse.ArgumentParser(
    prog= 'Mac Address',
    description= 'Command line Mac Address Lookup'
)

parser.add_argument('mac', help='Require https secure connection and query')

args =parser.parse_args()

mac = args.mac 

url = 'http://macvendors.co/api/' + mac

request = urllib.request.urlopen(url)
#read = codecs.getread('utf-8')
jrequest = json.load(request)
print('Company name: ' + jrequest['result']['company'])
print('Address: ' + jrequest['result']['address'])
