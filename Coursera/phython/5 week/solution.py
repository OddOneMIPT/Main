import socket
import time

class ClientError(Exception):
    pass


        

class Client:
    


    
    def __init__(self, ip_address, port, timeout = None ):
        #from solution import ClientError as ClientError
        self.__ip_address = ip_address
        self.__port = port
        self.__timeout = timeout
        ip_address_list = list(ip_address.split('.'))
        for i in ip_address_list:
            if len(ip_address_list) != 4:
                raise ClientError("Неправильный IP-адрес")
            if not i.isdigit():
                raise ClientError("Неправильный IP-адрес")
        if port <= 1999 or port >= 65536:
            raise ClientError('Вы ввели неверный порт, значение от 2000 до 65535')
        self.__sock = socket.create_connection((self.__ip_address, self.__port), self.__timeout)


    def put(self, key, value = None, timestamp = None):
        if not value and not timestamp:
            text = f'put {key}\n'
            self.__sock.sendall(text.encode("utf8"))
            data = self.__sock.recv(1024).decode('utf8')
            if 'ok\n\n'== data:
                pass
            else:
                raise ClientError
        elif timestamp == None:
            text = f'put {key} {value} {int(time.time())}\n'
            self.__sock.sendall(text.encode("utf8"))
            data = self.__sock.recv(1024).decode('utf8')
            if 'ok\n\n'== data:
                pass
            else:
                raise ClientError
        elif value == None:
            raise ClientError("Введите value")
        else:
            text = f'put {key} {value} {timestamp}\n'
            self.__sock.sendall(text.encode("utf8"))
            data = self.__sock.recv(1024).decode('utf8')
            if 'ok\n\n'== data:
                pass
            else:
                raise ClientError


    def get(self, key):
        text = f'get {key}\n'
        self.__sock.sendall(text.encode("utf8"))
        answer = self.__sock.recv(4024).decode('utf8')
        if 'ok' in answer and key in answer:
            answer = list(answer[3:].split())
            diction = {}
            for i in range(0,len(answer), 3):
                if answer[i] in diction:
                    diction[answer[i]].append((int(answer[i+2]), float(answer[i+1])))
                else:
                    diction[answer[i]] = [(int(answer[i+2]), float(answer[i+1]))]
            for key in diction:
                diction[key].sort(key=lambda i: i[0])
            return diction
        if key == '*' and 'ok' in answer:
            answer = list(answer[3:].split())
            diction = {}
            for i in range(0,len(answer), 3):
                if answer[i] in diction:
                    diction[answer[i]].append((int(answer[i+2]), float(answer[i+1])))
                else:
                    diction[answer[i]] = [(int(answer[i+2]), float(answer[i+1]))]
            for key in diction:
                diction[key].sort(key=lambda i: i[0])
            return diction
        if answer == 'ok\n\n':
            return {}
        raise ClientError('Что-то не так')
            


        
cl = Client('127.0.0.1', 8181, 15)
cl.get('palm.cpu')