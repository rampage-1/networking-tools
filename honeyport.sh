#!/bin/bash
# for https://wildwesthackinfest.com/antisyphon/active-defense-cyber-deception-john-strand/
# not an original work

echo "Started"

while [ 1 ]
do
        IP=`nc -nvl 1025 2>&1 1>/dev/null | grep "received" | awk -F '[] []' '{print $3;}'`
        iptables -A INPUT -p TCP -s $IP -j DROP
        echo -- $IP has been blocked!

done
