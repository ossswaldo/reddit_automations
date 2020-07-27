import re, os
import subprocess




while True:

    full_results = [re.findall('^[\w\?\.]+|(?<=\s)\([\d\.]+\)|(?<=at\s)[\w\:]+', i) for i in os.popen('arp -a')]
    final_results = [dict(zip(['IP', 'LAN_IP', 'MAC_ADDRESS'], i)) for i in full_results]
    final_results = [{**i, **{'LAN_IP':i['LAN_IP'][1:-1]}} for i in final_results]

    # print(final_results)
    counter= 0
    IP_DEVICE = 'f8:4e:73:ce:57:25'
    for key in final_results:
        # print(final_results[0]['MAC_ADDRESS'])
        connected_ip = final_results[counter]['MAC_ADDRESS']
        if(final_results[counter]['MAC_ADDRESS'] == IP_DEVICE):
            print("device connected")
        if connected_ip == IP_DEVICE:
            subprocess.Popen(["say", "connected to the network"])
        if connected_ip != IP_DEVICE:
            subprocess.Popen(["say", "device not connected"])
        counter +=1
