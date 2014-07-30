#!/bin/bash
#Program:
#	User input a filename, program will check the followings:
#	1. exist? 2.file/directory? 3.file permissions
#History:
# 2005/08/25	VBird	First release
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

#Determine whether the user actually enter a filename (some string)
echo -e "Please input a filename, I will check the filename's type and \ permission. \n\n"
read -p "Input a filename: " filename
test -z $filename && echo "You MUST input a filename." && exit 0

#Test whether the file exists. If not, print the message and exit.
test ! -e $filename && echo "The filename $filename DOES NOT exist" && exit 0

#Determine file properties:
# PART OF THE CODES
test -f $filename && filetype="regular file"

echo "The filename: $filename is a $filetype"


