import subprocess
import sys
import os

# ip = sys.argv[1]
#
# # ping ip
# p = subprocess.Popen(['ping', ip , '-c1'], stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE)
# out, err = p.communicate()
# # arp list
# p = subprocess.Popen(['arp', '-n'], stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE)
# out, err = p.communicate()
# try:
#     arp = [x for x in out.split('\n') if ip in x][0]
# except IndexError:
#     sys.exit(1)     # no arp entry found
# else:
#     # get the mac address from arp list
#     # bug: when the IP does not exists on the local network
#     # this will print out the interface name
#     print ('F8:4E:73:CE:57:25 '.join(arp.split()).split()[2])
######
# import socket
# IP1 = socket.gethostbyname(socket.gethostname()) # local IP adress of your computer
# IP2 = socket.gethostbyname('Oswaldo’s MacBook Pro') # IP adress of remote computer
#
# print(IP1)
# print(IP2)
#####
# devices = []
# for device in os.popen('arp -a'): devices.append(device)
#
# print(os.popen('arp -a'))

####
import re
full_results = [re.findall('^[\w\?\.]+|(?<=\s)\([\d\.]+\)|(?<=at\s)[\w\:]+', i) for i in os.popen('arp -a')]
final_results = [dict(zip(['IP', 'LAN_IP', 'MAC_ADDRESS'], i)) for i in full_results]
final_results = [{**i, **{'LAN_IP':i['LAN_IP'][1:-1]}} for i in final_results]
print(full_results)
# print(final_results)
