import socket
from struct import *
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('dk02.uncc.edu', 25002))

# Build format string for struct
# < signals little endian
# data header + 30*(targetId,  x,y,z, height,width,facing, 10 appearance vars)
data_format = '<qi' + 30*('qffffff' + 10*'f')
data_size = calcsize(data_format)

while True:
    raw_data = client_socket.recv(data_size)
    tframe = unpack(data_format, raw_data)

    timestamp = tframe[0];
    nTargets = tframe[1];

    print 'Time: ' + str(timestamp) + 'ms, nTargets: ' + str(nTargets)

    for iTarget in range(0,nTargets):
        idx = 2+17*iTarget
        targetId = tframe[idx]
        targetX = tframe[idx+1]
        targetY = tframe[idx+2]
        targetZ = tframe[idx+3]
        targetHeight = tframe[idx+4]
        targetWidth = tframe[idx+5]
        targetFacing = tframe[idx+6]
        targetApp = tframe[ (idx+7):(idx+17) ]
        print str(targetId) + ' is at ' + str(targetX) + ',' + str(targetY)