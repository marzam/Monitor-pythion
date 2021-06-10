#!/home/mzamith/Apps/anaconda3/bin/python
from pcapfile import savefile
import dpkt
import binascii
import sys
#apt install libcap2-bin tshark
# pip install pyshark

#pip install pcapfile
#pip install dpkt
#https://dpkt.readthedocs.io/en/latest/_modules/dpkt/radiotap.html

import pyshark

def printProbeRequestFrame(rec):
    info = rec.frame_info
    radiotap = rec.radiotap
    wlan_radio = rec.wlan_radio
    wlan = rec.wlan
    wlan_mgt = rec['wlan.mgt']
    print('Frame info: ', info)
    print('Radio header:', radiotap)
    print('802.11 radio information: ', wlan_radio)
    print('IEEE 802.11 (wlan)', wlan)
    print('IEEE 802.11 Wireless Management', wlan_mgt)



if __name__ == "__main__":

#    cap = pyshark.FileCapture('/home/mzamith/Documents/Works/UFRRJ/disciplinas/TM411-Redes/datasets/motorola_g7_power_probes_filtered_-40dbm.pcap', only_summaries=True)
    #cap = pyshark.FileCapture('/home/mzamith/Documents/Works/UFRRJ/disciplinas/TM411-Redes/datasets/motorola_g7_power_probes_filtered_-40dbm.pcap', only_summaries=True)
    cap = pyshark.FileCapture('/home/mzamith/Documents/Works/UFRRJ/disciplinas/TM411-Redes/datasets/motorola_g7_power_probes_filtered_-40dbm.pcap')
    for rec in cap:
        #print(dir(rec))
        #print(dir(wlan))
        #print(rec)
        printProbeRequestFrame(rec)


        sys.exit(-1)


'''
    print(dir(cap[1]))
    print('Comprimento da msg:', cap[0].captured_length, ' in bytes')
    print('Epoch time:', cap[0].sniff_timestamp)
    info = cap[0].frame_info
    print('Info: ', info.protocols)
    print('Show:', cap[0].show)
    if info.protocols == 'radiotap:wlan_radio:wlan':
        print('ok')
'''
