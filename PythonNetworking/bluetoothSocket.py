"""
A simple Python script to send messages to a server over Bluetooth using
Python sockets (with Python 3.3 or above).

Needs server to run python bluetooth code, available at http://blog.kevindoran.co/bluetooth-programming-with-python-3/
"""

import socket

serverMACAddress = 'A0:E6:F8:BA:80:06'
port = 3
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))
while 1:
    text = input()
    if text == "quit":
        break
    s.send(bytes(text, 'UTF-8'))
s.close()
