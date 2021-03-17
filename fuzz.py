#!/usr/bin/python3 

import requests
import re
from pwn import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

proxies = {'https':'http://127.0.0.1:8080'}

def read_file():
	wordlist=input("Specify a Wordlist: ")
	wordlist1 = wordlist.strip("\n")
	# print(wordlist)
	with open (f'{wordlist1}') as f:
		lines = [line.rstrip() for line in f]
		return lines

payload = read_file()
# print(len(payload))
log.success("POSSIBLE FILES:")
for i in range(len(payload)):
	# print(payload[i])
	url = f"https://freeflujab.htb/?{payload[i]}"
	r = requests.get(url,proxies=proxies,verify=False)
	response = r.text
	# print(response)
	if('Flu vaccination is available' not in response):
		print(payload[i])


