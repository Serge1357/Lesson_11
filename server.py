import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)
Dict = {"Hi": "Hello", "How are you?": "fine", "see you later": "good luck"}
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    print(str(data))
    conn.send(Dict[data.decode()].encode())
conn.close()
