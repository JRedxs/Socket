import socket
import logging

HOST = '0.0.0.0'

PORT = 5000

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as serveur:
    logging.info("Connexion au serveur...")
    serveur.bind((HOST,PORT))
    serveur.listen(1)
    logging.info("Attente de connexion")
    client, addr = serveur.accept()
    logging.info("Connexion OK ")
    while True:
        message = client.recv(1024).decode()
        print(f'Message ok : {message}')

        if message.lower() == 'ping':
            reponse = 'pong'
        elif message.lower() == 'pong':
            reponse = 'pong'
        else:
            print('Message non valide')
        client.sendall(reponse.encode())
