import socket
import logging

HOST = '0.0.0.0'
PORT = 5000

def jouer_chorale(ordre_chanteurs, choral):
    chanteurs = ["A", "B", "C"]
    chanteur_index = 0
    triangle_count = 0
    output = ""
    for i in range(len(ordre_chanteurs)):
        chanteur = chanteurs[chanteur_index]
        if chanteur == choral:
            output += chanteur + choral + " "
        else:
            output += chanteur + " "
        chanteur_index += 1
        if chanteur_index == 3:
            chanteur_index = 0
            triangle_count += 1
            if triangle_count == 3:
                output += "/ "
                triangle_count = 0
    return output

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serveur:
    logging.info("Démarrage du serveur...")
    serveur.bind((HOST, PORT))
    serveur.listen(1)
    logging.info("En attente de connexions...")
    client, adresse = serveur.accept()
    logging.info(f"Connexion établie avec {adresse}")
    while True:
        ordre_chanteurs = client.recv(1024).decode().strip()
        logging.info(f"Ordre des chanteurs reçu : {ordre_chanteurs}")
        if len(ordre_chanteurs) >= 6:
            choral = client.recv(1024).decode().strip()
            logging.info(f"Choral reçu : {choral}")
            resultat = jouer_chorale(ordre_chanteurs, choral)
            client.sendall(resultat.encode())
        else:
            client.sendall(b"Ordre des chanteurs invalide.")
