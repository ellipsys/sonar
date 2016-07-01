#!/usr/bin/env python
from scapy.all import *

APs = [] 

def PacketHandler(pkt):
  if pkt.haslayer(Dot11):
    if pkt.type == 0 and pkt.subtype == 8 :
      if pkt.addr2 not in aPs:
        APs.append(pkt.addr2)
        print "MAC: %s con SSID: %s " %(pkt.addr2, pkt.info) 
      
sniff(iface = "mon0", prn = PacketHandler)
