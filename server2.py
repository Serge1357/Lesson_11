import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024).decode()
    k = 0
    for t in data:
        if t == " ":
            k += 1
    k += 1
    print(str(data))
    conn.send(("кількість слів - " + str(k)).encode())
    #conn.send(str(k).encode())
conn.close()