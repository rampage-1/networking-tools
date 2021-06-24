#!/bin/bash
# for https://academy.tcm-sec.com/p/practical-ethical-hacking-the-complete-course
# not an original work

if [ "$1" == "" ] 
then 
echo "usage: ./ipsweep.sh 192.168.4"

else
for ip in `seq 1 254` ; do 
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done
fi
