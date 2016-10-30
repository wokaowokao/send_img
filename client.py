import os
import socket
import time
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cv2.imwrite('../xx.png',frame)
cap.release()
cv2.destroyAllWindows()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 10000)
sock.connect(server_address)

start = time.time()
try:
    with open(r'../xx.png', 'rb') as f:
        message = f.read()
        sock.sendall(message)
finally:
    sock.close()
os.remove('../xx.png')
end = time.time()
print('Total time: ', end-start)
