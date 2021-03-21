#!/usr/bin/env python3
#Mass Check Alexa Rank Tools Merupakan Tools Yang Berfungsi Mengecek Alexa Rank Suatu Website Secara Massal
#Alexa Rank Bulk Check Tool Is A Tool That Serves To Check The Alexa Rank Of A Website In Bulk
#Mass Check Alexa Rank Tools By Wan5550
#Contact Me? : wannaz.idn@gmail.com

import requests
import json
import os
from colorama import Fore, Back, Style
import time

def bersih():
	   linux = "clear"
	   windows = "cls"
	   os.system([linux,windows][os.name == "nt"])
bersih()

hijau = Fore.GREEN
merah = Fore.RED
cyan = Fore.CYAN
tai = Fore.YELLOW
biru = Fore.BLUE

time.sleep(1.50)

print(merah+"-----------------------------------")
print(Style.RESET_ALL)
print(cyan+"~#: Mass Check Alexa Rank Tools :#~")
print(Style.RESET_ALL)
print(merah+"-----------------------------------")
print(Style.RESET_ALL)
print(tai+"[+] Author : Wan5550")
print(Style.RESET_ALL)
print(tai+"[+] Github : github.com/wannazid")
print(Style.RESET_ALL)

input_list = input(biru+"[-] Open Your List Site (list_site.txt) : ")
print(Style.RESET_ALL)
open_site = open(input_list,"r").read().splitlines()
print(hijau+"Loading Check List "+"=",input_list)
time.sleep(4)
print(Style.RESET_ALL)
print(merah+"================================")
url = "https://d4rk5idehacker.or.id/api/alexarank.php?q="
for list in open_site:
	  req = requests.get(url+list).text
	  print(hijau)
	  print("Alexa Rank : "+list+" =",json.loads(req)['rank'])