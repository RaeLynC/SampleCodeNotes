#!/usr/bin/python
'''
    Simple socket server using threads
'''

import socket
import sys
from thread import *
import re

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port

#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client - send only takes string
    conn.send('Welcome to the server. Type something and hit enter\n') 

    #infinite loop so that function do not terminate and thread do not end.
    quit = re.compile('quit')
    while True:

        #Receiving from client
        data = conn.recv(1024)
        reply = 'OK...' + data
        print(data, 'quit', data==quit)
        if not data or (quit.match(data)):
            break

        conn.sendall(reply)

    #came out of loop
    print('client thread exiting')
    conn.close()

# Set up main fct:
#	1. Create and bind the socket
#	2. Spawn a new thread for each client connection.
#
if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'Socket created'

    #Bind socket to local host and port
    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

    print 'Socket bind complete'

    #Start listening on socket
    s.listen(10)
    print 'Socket now listening'

    #now keep talking with the client
    while 1:
        #wait to accept a connection - blocking call
        conn, addr = s.accept()
        print 'Connected with ' + addr[0] + ':' + str(addr[1])

        # start new thread takes 1st argument as a function name to be run
        # second is the tuple of arguments to the function.
        start_new_thread(clientthread ,(conn,))

    s.close()
