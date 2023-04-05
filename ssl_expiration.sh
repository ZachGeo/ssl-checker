#!/bin/bash

IFS=','
INPUT_FILE=$1
output=()

while read hostname port servername
do
	openssl_output=$(echo | openssl s_client -connect $hostname:$port -servername $servername 2> /dev/null |  openssl x509 -noout -enddate)

        month=$(echo $openssl_output | awk '{ print $1 }' | cut -d "=" -f2)
        day=$(echo $openssl_output | awk '{ print $2 }')
        year=$(echo $openssl_output | awk '{ print $4 }')

        expiration_date=$(date -d "${month} ${day} ${year}" "+%Y-%m-%d")
	
        echo $servername, $expiration_date

done < $INPUT_FILE
