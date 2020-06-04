#-----------------------------------------------
# socket_echo_server.py
#
# author  =  danu andrean
#
#------------------------------------------------

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
host = ''                   #kosong karena ini server jadi dia default ke localhost
port = 8080
print('connecting to {} port {}'.format(host,port))
sock.bind((host,port))

# Listen for incoming connections
sock.listen(5)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive data 
        data = connection.recv(1024)
        print(data)


        #send data // menggunakan funsi encode
        message = "Hay Yenny"
        connection.send(message.encode())  #ini sama dengan => connection.send(bytes(message,'utf-8'))

    finally:
        # Clean up the connection
        connection.close()

