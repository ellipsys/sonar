import csv
ssid=raw_input("SSID: ")
with open('db.csv','r') as f:
        router=csv.reader(f, delimiter=',')
        for row in router:
                a=row[2]
                b=a.startswith(ssid)
                if b:
                        print "***************************************************************"
                        print 'Network: '+row[2]+'\nPassword: '+row[3]+'\nIp adress: '+row[0]+'\nDevice: '+row[1]+'\n***************************************************************'
                        
                else:
                        pass
                        



            
                
