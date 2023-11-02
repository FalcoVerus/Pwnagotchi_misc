#!/bin/bash

/usr/bin/hcxpcapngtool /root/handshakes/*.pcap -o "/home/pi/hashes/allhashes.hc22000"

echo "Hash files got combined into a single file."
