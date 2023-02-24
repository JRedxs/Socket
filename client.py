import socket
import logging


HOST = "127.0.0.1"
PORT = 5000

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client:
    logging.info("Connexion en  cours...")
    client.connect((HOST,PORT))
    while True:

        message = input('Message : ')

        client.sendall(message.encode())

        reponse = client.recv(1024).decode()
        print(f'Reponse : {reponse}')