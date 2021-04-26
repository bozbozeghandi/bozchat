#!/usr/bin/python           # This is server.py file

import socket  # Import socket module
import threading
import pickle

cha = {}
name_set = set()


class Message:
    receiver = None
    msg = None
    sender = None


def sending(c):
    c.send(b"say your name\n")
    name = c.recv(1024).decode("utf-8")
    name_set.add(name)
    cha[name] = c
    while True:
        pickled_message = c.recv(1024)
        msg = pickle.loads(pickled_message)
        if msg.msg == '.':
            msg.msg = str(name_set)
            msg.receiver = name
            msg.sender = 'server'
            c.send(pickle.dumps(msg))
        if msg.msg == 'dl_me':
            name_set.discard(msg.sender)
        else:
            cha[msg.receiver].send(pickled_message)


s = socket.socket()  # Create a socket object
host = "0.0.0.0"  # Get local machine name
port = 12345  # Reserve a port for your service.

s.bind((host, port))  # Bind to the port
s.listen(5)  # Now wait for client connection.
while True:
    c, addr = s.accept()  # Establish connection with client.
    x = threading.Thread(target=sending, args=(c,))
    x.start()
