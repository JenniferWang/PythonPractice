#!/bin/bash
#Program:
#	Program creates three files, which named by user's input and date command
#History:
#2014/07/28 Jennifer Wang First release
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

echo -e "I will use 'touch' command to create 3 files"
read -p "Input your filename: " fileuser

# In order to avoid the user tap 'Enter' carelessly, exam whether the variable has been set before.
filename=${fileuser:-"filename"}

date1=$(date -d "2 days ago" "+%Y%m%d") #The day before yesterday
date2=$(date -d "1 days ago" "+%Y%m%d")  #Yesterday
date3=$(date "+%Y%m%d")					  #Today
file1=${filename}${date1}
file2=${filename}${date2}
file3=${filename}${date3}

touch "$file1"
touch "$file2"
touch "$file3"

