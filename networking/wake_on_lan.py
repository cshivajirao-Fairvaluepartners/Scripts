import sys
from socket import *

def wake_on_lan(mac_addr):

    # Build our magic packet
    p = str()
    for _ in range(6):
        p += chr(255)
    for byte in mac_addr.split(':'):
        p += chr(int(byte, 16))
    for _ in range(16):
        p += mac_addr

    # UDP broadcast to everything
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.setsockopt(SOL_SOCKET, SO_BROADCAST, True)
    sock.sendto(p, ('255.255.255.255', 9))
    sock.close()

if len(sys.argv) > 1:
    wake_on_lan(sys.argv[1])
    print "WOL packet broadcasted for " + sys.argv[1]
else:
    print "Specify a MAC address to wake up, ex: \"python wake_on_lan.py 03:ab:4e:81:fd:c7\""
