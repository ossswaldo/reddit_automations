import sys
import subprocess
import os
from decouple import config


# import socket
# print(socket.gethostbyname(socket.gethostname()))



# IP_NETWORK = config('192.168.254.17')

IP_NETWORK = config('IP_NETWORK')
IP_DEVICE = config('IP_DEVICE')

proc = subprocess.Popen(["ping", IP_NETWORK],stdout=subprocess.PIPE)

while True:
  line = proc.stdout.readline()
  if not line:
    break
  #the real code does filtering here
  connected_ip = line.decode('utf-8').split()[3]
  print(connected_ip)

  if connected_ip == IP_DEVICE:
      subprocess.Popen(["say", "connected to the network"])
