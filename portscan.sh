#!/bin/bash

# for port in {1..3000};do ---------use this when you wanna scan 
2>/dev/null echo > /dev/tcp/10.129.1.97/$1 #----------use #port in place of $1 in case of scan
if [ $? == 0 ]
then
	echo "$1 is open"
fi
# done
