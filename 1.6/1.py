import socket
sock = socket.socket()
sock.bind(('', 2222))
sock.listen(1)
conn, addr = sock.accept()
while True:
        data = conn.recv(1024)
        if not data or data == b'close': break
        conn.send(data)
conn.close
