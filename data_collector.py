#!/usr/bin/python3

import system_tool 
import network
import port
import client_browser
import mac_lookup

project = open('network-survival.txt', 'w')
project.write(system_tool.system())

if __name__ == "__main__":
    system_tool.system()
    network.network()
    port.port()
    client_browser.client()
    mac_lookup.mac()