#!/bin/sh
python3 -m info_script > /home/output/result.txt
cat /home/output/result.txt

echo "Press CTRL+C to exit"
while true 
do
    sleep 1
done