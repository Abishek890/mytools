#!/bin/bash


for i in {2..255};do
	ping -c 1 172.20.0.$i | grep "bytes from" | grep -v "Unreachable" &
done