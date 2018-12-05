from socket import *
import struct
HOST = '127.0.0.1'
PORT = 8888
target_idx = 0
s = socket(AF_INET,SOCK_DGRAM)
s.bind((HOST,PORT))

print ('...waiting for message..')
while True:
    data,address = s.recvfrom(1328)
    print (data,address)
    idx = struct.unpack('>i',data)
    target_idx = target_idx + 1
    if target_idx != idx[0]:
        #print (target_idx,idx[0],idx[0]-target_idx)
        target_idx = idx[0]

s.close()
