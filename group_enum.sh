#!/bin/bash
echo "[+]USAGE:THIS CAN LIST ALL THE FILES THAT IS OWNED BY THE GROUP ARE IN...very useful when you are in multiple groups and you need to see it in a single folder"
echo "[INFO]The script is not allowd to link some files which are owned by the user "
for files in $(groups);do
        if [ $files == "test" ];then
                continue
        fi
        mkdir $files 
        find / -group $files 2>/dev/null > ${files}.txt
        number=`wc -l ${files}.txt | awk -F " " '{print $1}'`
        echo "-----$number-----$files-------"
        for i in $(seq "$number");do 
                hello=`sed -n "$i"p "$files".txt`
                ln -s $hello $files/ 2>/dev/null
        done
	valid=`ls -l $files | wc -l `
	echo "[+]files linked-----$((valid - 1))"
	printf "\n"
done
