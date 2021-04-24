import socket
with socket.socket() as sock:
    sock.bind(("", 10001))
    sock.listen()
    while True:
        conn, addr = sock.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if data == b'ok':
                    conn.send(b'error\nwrong command\n\n')
                else:
                    conn.send(b'error\nwrong command\n\n')
