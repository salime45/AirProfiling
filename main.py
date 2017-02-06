
import scapy_http.http as scapyh
from model import Perfil
from scapy.utils import rdpcap
from scapy.layers.inet import IP


def savePcap(path):
    
    packets =  rdpcap(path)
    
    for i in range(len(packets)):
        
        p = packets[i]
        print("MAC: " + p.src)
        print("TIME: " + str( p.time))
        print("IP: " +  packets[i][IP].dst)

        if scapyh.HTTPRequest in p:            
            print("User-Agent: " + str(scapyh._get_field_value(p[scapyh.HTTPRequest], "User-Agent")))
            print("Host: " + str(scapyh._get_field_value(p[scapyh.HTTPRequest], "Host")))

        print("=====================================================================================\n")
        '''
        perfil = Perfil()
        perfil.mac = p.src
        '''

        
        
savePcap("/home/ultra/Downloads/20170129-2.pcapng")


