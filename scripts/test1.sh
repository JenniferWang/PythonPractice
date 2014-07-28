#!/bin/bash
#Program:
#	User inputs first name and last name. Program shows full name
#History:
#2014/07/28 Jennifer First release
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

read -p "First name " firstname
read -p "Last name " lastname
echo -e "\nFull name is: $firstname $lastname" # -e enable interpretation of backslash escapes
