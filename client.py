#-----------------------------------------------
# socket_echo_client.py
#
# author  =  Yenny Rahmawati
#
#------------------------------------------------


import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
host = '192.168.43.54'
port = 8080
print('connecting to {} port {}'.format(host,port))
sock.connect((host,port))

try:

    # Send data // menggunakan encoder utf-8
    message = "okay"
    sock.send(bytes(message,'utf-8'))    #ini sama dengan =>  sock.send(message.encode())

    #receive data
    data = sock.recv(1024)
    print(data)


finally:
    print('closing socket')
    sock.close()

