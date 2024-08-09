import sys
from datetime import datetime as dt
import socket

print(sys.version)
print(dt.now())

HOST = '127.0.0.1'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print('Invalid amount of arguments')
    print('Syntax: Python3 scanner.py <ip>')

print('-' * 50)
print("Scanning Target: " + target)
print('Time Started: ' + str(dt.now()))
print('-' * 50)

try:
    for PORT in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, PORT))
        if result == 0:
            print(f'Port {port} is open')
        s.close()

except KeyboardInterrupt:
    print('\n Exiting program')
    sys.exit()

except socket.gaierror:
    print('\n Hostname could not be resolved')
    sys.exit()

except socket.error:
    print('\n Could not connect to server')
    sys.exit()