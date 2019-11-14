import socket

def get_hostname_ip():
    try:
        hostname=socket.gethostname()
        hostip=socket.gethostbyname(hostname)
        print("Hostname :",hostname)
        print("IP :",hostip)
        
         print("SUCCESS")
    except:
        print('unable to get Hostname and IP')

get_hostname_ip()
              
