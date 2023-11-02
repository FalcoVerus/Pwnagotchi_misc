#!/bin/bash

filecount_before=$(ls -lA /home/pi/hashes/|grep -v '^d' | wc -l)
counter=0
for file in /root/handshakes/*; do
	if [ -f "$file" ]; then
		base_name=$(basename "$file")
		hash_file="${base_name%.*}.hash"
		/usr/bin/hcxpcapngtool "$file" -o "/home/pi/hashes/$hash_file"
		counter=$((counter+1))
	fi
done

filecount_after=$(ls -lA /home/pi/hashes/|grep -v '^d' | wc -l)
filecount=$((filecount_after - filecount_before))

echo "Hash generation is done. $counter number of files have been processed. $filecount hashes have been acquired."
