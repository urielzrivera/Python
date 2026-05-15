#!/usr/bin/env pythonend = timer()

import errno, sys
from socket import *


if (len(sys.argv) > 1):
    # Assign the first argument (server) to 'remote_host'
    remote_host = sys.argv[1]
    # Assign the second argument (port) to 'server_port'
    server_port = int(sys.argv[2])

    # Open a TCP socket
    portconn = socket(AF_INET, SOCK_STREAM)
    try:
        portconn.connect((remote_host, server_port))
        portconn.shutdown(2)

        print "Success. Connected to " + remote_host + " on port: " + str(server_port)
    except:
        print "Failure. Cannot connect to " + remote_host + " on port: " + str(server_port)
        sys.exit(errno.EPERM)
    # Close socket connection
    portconn.close()
else:
    print "Usage : python portcheck.py <host> <port>"
