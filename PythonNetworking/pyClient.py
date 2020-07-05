import socket, traceback
import time, os
from datetime import datetime

host = ''
port = 5001
 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))
 
#used for debugging
 
print("Success binding")


while 1:
    #get the message as utf text
    message, address = s.recvfrom(8192) # For best match with hardware and network realities, the value of bufsize should be a relatively small power of 2
    messageString = message.decode("utf-8")
    #print to console
    print(messageString)   
    print("payload size of: "+ str(len(messageString)))
    print()
    
    

        
        
