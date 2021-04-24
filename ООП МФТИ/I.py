import socket
with socket.create_connection(("127.0.0.1", 10001)) as sock:
    sock.sendall("ok".encode("utf8"))
    answer = b''
    #while not answer:
    data = sock.recv(1024)
    data = data.decode("utf8")
    if 'ok' in data:
        print(1)
    else:
        print(0)
