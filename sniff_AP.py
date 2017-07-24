#!/usr/bin/env python
import requests as rq

from scapy.all import *

APs = [] 
def fabricante(mac):
    mac = str(mac).replace(":","-")
    link = "http://api.macvendors.com/"+mac
    r = rq.get(link)
    return r.content

def PacketHandler(pkt):
  if pkt.haslayer(Dot11):
    if pkt.type == 0 and pkt.subtype == 8 :
      if pkt.addr2 not in APs:
        APs.append(pkt.addr2)
        mac = pkt.addr2
        fab = fabricante(mac)
        print "MAC: %s SSID: %s BUILD: %s" %(pkt.addr2, pkt.info,fab)
   
      
sniff(iface = "wlan1", prn = PacketHandler)

