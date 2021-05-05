#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.system("apt-get install figlet")
os.system("apt-get install nmap")
os.system("clear")
os.system("figlet Port Scanner")
print("""

#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                SIMPLE PORT SCANNER                  #
#                BY SASUKE2635                        #
#                WELCOME PORT SCANNER                 #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################

choose one of the following options

1)Fast Scan
2)Getting Information About Service and Version
3)Getting information about the operating system
4)Advanced Search (Requires Proxy)

""")
islemno = input("which:")
if(islemno=="1"):
    hedefip = input("TargetIp:")
    os.system("nmap " + hedefip)
elif(islemno=="1"):
    hedefip = input("TargetIp:")
    os.system("nmap -sS -sV" + hedefip)
elif(islemno=="1"):
    hedefip = input("TargetIp:")
    os.system("nmap -O" + hedefip)
elif(islemno=="1"):
    hedefip = input("TargetIp:")
    proxy1 = input("Enter Your Proxy Addresses (Example: socks4: //127.0.1.0), https://127.0.1.0:")
    os.system("nmap -Pn " + hedefip + " -sV -sS -v -T4 -O --proxy" + proxy1 )
