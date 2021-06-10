#!/home/mzamith/Apps/anaconda3/bin/python
import sys
#apt install libcap2-bin tshark
# pip install pyshark

#pip install pcapfile
#pip install dpkt
#https://dpkt.readthedocs.io/en/latest/_modules/dpkt/radiotap.html

import pyshark




if __name__ == "__main__":
    capture = pyshark.LiveCapture(output_file="pysharkCap.pcap", interface='wlx48ee0cd9b6ee')
    for packet in capture.sniff_continuously():
        print(packet)
