import os
import socket
import hashlib
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(1)

def get_num(num):
    if os.path.exists(r'd:\img\\' + num + '.png'):
        num = int(num) + 1
        num = str(num)
        return get_num(num)
    else:
        return num

while True:
    print('Waiting for a connection')
    num = '1'
    num = get_num(num)
    connection, client_address = sock.accept()
    size = 0
    try:
        i = 0
        _f = open('d:\img\\' + num + '.png','wb')
        while True:
            data = connection.recv(65536)
            _f.write(data)
            #print('Received data: "%s"' % data)
            i += 1
            if data:
                size += len(data)
                #print(data)
                #cnt += data
                if i % 10000 == 0:
                    print('Current loop: ', i)
                #print('[%s]' % data)
            else:
                print('Done!')
                break
        print('I:', i)
        print('Total size: ', size)
        #print('Hash of received data :', hashlib.md5(cnt).hexdigest())
    finally:
        connection.close()
