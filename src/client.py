import socket  # Import socket module
import threading
import pickle


class Message:
    receiver = None
    msg = None
    sender = None


isalive = True


def receiving(c):
    while isalive:
        msg = pickle.loads(c.recv(1024))
        print(f"{msg.sender}: ", msg.msg)



s = socket.socket()  # Create a socket object
host = socket.gethostname()  # Get local machine name
port = 12345  # Reserve a port for your service.

print("Connecting to ", host, port)
s.connect((host, port))
msg = s.recv(1024)
print("server", msg.decode("utf-8"))
name = input()
s.send(name.encode("utf-8"))
target = input("Enter target: ")
x = threading.Thread(target=receiving, args=(s,), daemon=True)
x.start()
while True:
    msg = Message()
    msg.msg = input()
    if msg.msg == 'exit':
        isalive = False
        msg.msg = 'dl_me'
        msg.receiver = 'server'
        msg.sender = name
        s.send(pickle.dumps(msg))
        break
    elif msg.msg == '*':
        target = input("Enter target: ")
    msg.sender = name
    msg.receiver = target
    s.send(pickle.dumps(msg))
