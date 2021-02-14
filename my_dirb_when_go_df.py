#!/usr/bin/python3

import requests
import re
from pwn import *

with open('common1.txt') as fp:
   for cnt, line in enumerate(fp):
       filename=line.strip()
       print(filename)
       url="http://oz.htb/{}".format(filename)
       r=requests.get(url)
       response=r.text
       # print(response)
       if("<" in response):
       	log.success("GOT ONE:{}".format(filename))
