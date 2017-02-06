
import scapy_http.http as scapyh
import datetime;

from scapy.utils import rdpcap
from scapy.layers.inet import IP


def savePcap(path):
    
    packets =  rdpcap(path)
    
    for i in range(len(packets)):
        
        p = packets[i]
        print("MAC: " + p.src)
        print("TIME: " + getDate(p.time))
        print("IP: " +  packets[i][IP].dst)

        if scapyh.HTTPRequest in p:            
            print("User-Agent: " + str(scapyh._get_field_value(p[scapyh.HTTPRequest], "User-Agent")))
            print("Host: " + str(scapyh._get_field_value(p[scapyh.HTTPRequest], "Host")))

        print("=====================================================================================\n")
        '''
        perfil = Perfil()
        perfil.mac = p.src
        '''

def getDate(time):
    return datetime.datetime.fromtimestamp(time).strftime('%d-%m-%Y %H:%M:%S')
        
        
savePcap("cap/example.pcapng")



