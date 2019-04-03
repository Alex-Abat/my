import socket
sock = socket.socket()
sock.bind(('',2222))
sock.listen(10)
while True:
        conn, addr = sock.accept()
        data = conn.recv(1024)
        if data != b'' or data != b'close':
                conn.send(data)
        conn.close()
