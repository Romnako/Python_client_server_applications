import argparse
import socket
import json

ADDRESS = 'localhost'
PORT = 7777
CONNECTION = 10


def get_server_socket(addr, port):
    s = socket.socket()
    s.bind((addr, port))
    s.listen(CONNECTION)
    return s


def client_socket(addr, port):
    s = socket.socket()
    s.connect((addr, port))
    return s


def send_data(recipient, data):
    recipient.send(json.dumps(data).encode('utf-8'))


def get_data(sender):
    return json.loads(sender.recv(1024).decode('utf-8'))


def create_parser():
    parser = argparse.ArgumentParser(
        description='JSON instant messaging'
    )

    parser_group = parser.add_argument_group(title='Parametres')
    parser_group.add_argument('-a', '--addr', default=ADDRESS, help='IP address')
    parser_group.add_argument('-p', '--port',type=int, default=PORT, help='TCP port')

    return parser