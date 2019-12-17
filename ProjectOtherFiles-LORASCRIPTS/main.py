import machine
import math
import network
import os
from network import LoRa
import socket
import ubinascii
import time
import gc
from machine import RTC
from machine import SD
from L76GNSS import L76GNSS
from pytrack import Pytrack
import struct
import utime #utime

time.sleep(2)
gc.enable()

py = Pytrack()
l76 = L76GNSS(py, timeout=30)

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
# create an ABP authentication params
dev_addr = struct.unpack(">l", ubinascii.unhexlify('26011303'))[0]
nwk_swkey = ubinascii.unhexlify('D249E754D79DA754328ADA442E54772A')
app_swkey = ubinascii.unhexlify('DF779280946F590A87A902B7474F02C9')
print("Welcome!")
lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))

while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')
print("Connected!")

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

while (True):
    coord = l76.coordinates()
    lat, lon = coord
    print(lat)
    print(lon)
    #print(coord)
    s.setblocking(True)
    #msg = lat + ',' + lon
    #msg = coord
    #s.send(b'Hello')
    #s.send(int(msg))
    s.send(b''+str(lat)+','+str(lon)) ## Send last known coordinates
    time.sleep(1)
    s.setblocking(False)
    time.sleep(9)
